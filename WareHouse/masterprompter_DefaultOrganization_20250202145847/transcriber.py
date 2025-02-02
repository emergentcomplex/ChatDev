'''
Uses the Whisper 'tiny' model to transcribe audio to text.
'''
import whisper
class Transcriber:
    def __init__(self):
        self.model = whisper.load_model("tiny")
    def transcribe_audio(self, audio_file):
        print("Transcribing audio...")
        try:
            result = self.model.transcribe(audio_file)
            return result['text']
        except Exception as e:
            print(f"An error occurred during transcription: {e}")
            return ""