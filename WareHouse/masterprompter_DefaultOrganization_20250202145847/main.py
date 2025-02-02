'''
Main application file that orchestrates the workflow using a console-based interface.
'''
from audio_recorder import AudioRecorder
from transcriber import Transcriber
from openai_handler import OpenAIHandler
from text_to_speech import TextToSpeech
class MainApp:
    def __init__(self):
        self.recorder = AudioRecorder()
        self.transcriber = Transcriber()
        self.openai_handler = OpenAIHandler()
        self.tts = TextToSpeech()
    def update_console(self, text):
        print(text, end='', flush=True)
    def start(self):
        try:
            self.update_console("Recording started...\n")
            audio_file = self.recorder.record_audio()
            if audio_file is None:
                self.update_console("Recording failed.\n")
                return
            self.update_console("Recording stopped. Processing audio...\n")
            processed_file = self.recorder.trim_silence(audio_file, "processed_audio.wav")
            if processed_file is None:
                self.update_console("Audio processing failed.\n")
                return
            self.update_console("Transcribing audio...\n")
            transcribed_text = self.transcriber.transcribe_audio(processed_file)
            if not transcribed_text:
                self.update_console("Transcription failed.\n")
                return
            self.update_console(f"Transcribed Text:\n{transcribed_text}\n")
            self.update_console("Sending to OpenAI API...\n")
            response = self.openai_handler.send_request(transcribed_text, self.update_console)
            if not response:
                self.update_console("Failed to get response from OpenAI API.\n")
                return
            self.update_console("\n")
            self.update_console("Converting response to speech...\n")
            self.tts.convert_and_play(response)
            self.update_console("Done.\n")
        except Exception as e:
            self.update_console(f"An error occurred: {e}\n")
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    app = MainApp()
    app.start()