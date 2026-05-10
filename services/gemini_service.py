import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_response(user_prompt, system_prompt=""):

    final_prompt = f"""
    {system_prompt}

    User Question:
    {user_prompt}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=final_prompt
    )

    return response.text