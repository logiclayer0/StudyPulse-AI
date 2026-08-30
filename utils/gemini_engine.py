import os
import json
from groq import Groq

def generate_study_materials(content_text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is missing.")
        
    client = Groq(api_key=api_key)
    
    prompt = f"""
    You are an expert AI educator. Analyze the provided text thoroughly and generate a comprehensive study packet in JSON format.
    
    The JSON output must strictly contain the following keys:
    1. "summary": A detailed, deep concept explanation covering key theories, terms, and context.
    2. "fun_facts": An array of 3 interesting facts or real-world applications derived from the text.
    3. "flashcards": An array of objects with "question" and "answer" fields for memory retention.
    4. "pyqs": An array of objects with "question" and "answer" fields for exam-style questions with detailed answers.
    5. "quizzes": An array of 3 multiple-choice question objects containing:
       - "question"
       - "options" (array of 4 strings)
       - "correct_option_index" (integer 0 to 3)
       - "explanation" (detailed reason why the option is correct)

    Content Source:
    {content_text}
    """
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that outputs strict JSON."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.2
    )
    
    return json.loads(response.choices[0].message.content)