'''
Sends the transcribed text to OpenAI API and streams the response using a callback.
'''
import openai
import os
class OpenAIHandler:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')  # Load API key from environment variable
    def send_request(self, prompt, update_callback):
        print("Sending request to OpenAI...")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                stream=True
            )
            full_response = ''
            for chunk in response:
                if 'choices' in chunk:
                    delta = chunk['choices'][0]['delta']
                    if 'content' in delta:
                        text_chunk = delta['content']
                        update_callback(text_chunk)
                        full_response += text_chunk
            return full_response.strip()
        except Exception as e:
            print(f"An error occurred during OpenAI API call: {e}")
            return ""