import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

USE_MOCK = True

if not USE_MOCK:
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
    )


def generate_response(user_prompt, system_prompt=""):

    if USE_MOCK:
        mock_responses = {
            "What is KYC?":
                "KYC stands for Know Your Customer. It is a customer identity verification process used by banks and financial institutions.",

            "What is AML in banking?":
                "AML stands for Anti-Money Laundering. It helps prevent financial crimes and illegal money transfers."
        }

        return mock_responses.get(
            user_prompt,
            "Mock response generated"
        )

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