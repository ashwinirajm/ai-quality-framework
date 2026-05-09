import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


def generate_response(user_prompt, system_prompt=""):

    final_prompt = f"""
    {system_prompt}

    User Question:
    {user_prompt}
    """

    response = model.generate_content(final_prompt)

    return response.text