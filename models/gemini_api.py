import google.generativeai as genai
from config import config

def get_person_info(description):
    """
        For each person in the description, create a dictionary containing the person's information.

        Returns:
            person_info: A dictionary containing person information.
    """
    
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel(config.GEMINI_MODEL_NAME)

    prompt = config.GEMINI_PROMPT + description

    response = model.generate_content(prompt)

    return response.text
    