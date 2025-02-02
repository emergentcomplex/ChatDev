'''
Handles audio recording, stopping based on threshold, and trimming excess silence.
'''
import pyaudio
import wave
import audioop
import time
import os
import librosa
import soundfile as sf
import math
class AudioRecorder:
    def __init__(self, threshold=-35, silence_duration=2.5):
        self.threshold = threshold
        self.silence_duration = silence_duration
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.audio = pyaudio.PyAudio()
    def record_audio(self):
        try:
            stream = self.audio.open(format=self.format, channels=self.channels,
                                     rate=self.rate, input=True,
                                     frames_per_buffer=self.chunk)
            frames = []
            silence_start = None
            print("Recording...")
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
                rms = audioop.rms(data, 2)
                if rms > 0:
                    db = 20 * math.log10(rms)
                else:
                    db = -float('inf')
                if db < self.threshold:
                    if silence_start is None:
                        silence_start = time.time()
                    elif time.time() - silence_start >= self.silence_duration:
                        print("Silence detected. Stopping recording.")
                        break
                else:
                    silence_start = None
            stream.stop_stream()
            stream.close()
            wave_output_filename = "recorded_audio.wav"
            wf = wave.open(wave_output_filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            return wave_output_filename
        except Exception as e:
            print(f"An error occurred during recording: {e}")
            return None
    def trim_silence(self, input_file, output_file):
        try:
            print("Trimming silence from audio...")
            y, sr = librosa.load(input_file, sr=self.rate)
            trimmed, _ = librosa.effects.trim(y, top_db=35)
            sf.write(output_file, trimmed, sr)
            os.remove(input_file)
            return output_file
        except Exception as e:
            print(f"An error occurred during audio trimming: {e}")
            return None