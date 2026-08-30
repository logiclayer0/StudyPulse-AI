from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Say hello in one word"
)

print("✅ Response:", response.text)