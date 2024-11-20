# client1.py

import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def chat_gpt(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Specify the model you want
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
