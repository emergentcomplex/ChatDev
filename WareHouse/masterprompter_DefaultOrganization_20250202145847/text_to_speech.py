'''
Converts the OpenAI response text back to speech using pyttsx3 and plays it.
'''
import pyttsx3
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Adjust speech rate if needed
    def convert_and_play(self, text):
        try:
            print("Converting text to speech...")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"An error occurred during text-to-speech conversion: {e}")