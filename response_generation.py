import openai

class ResponseGeneration:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key  # Set your OpenAI API key

    def generate_response(self, question):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can use any GPT-3 model here
                prompt=question,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"[ERROR] Error generating response: {e}")
            return "Sorry, I couldn't understand the question."

