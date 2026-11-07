import os
import json
import re

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL_NAME = "gemini-3.8-flash"


def detect_ingredients(image_bytes, mime_type):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key missing. Check your .env file.")

    client = genai.Client(api_key=api_key)

    prompt = """
    Identify all clearly visible food ingredients in this image.
    Return ONLY a JSON array of simple ingredient names.

    Example: ["tomato", "onion", "potato", "carrot"]

    Do not guess hidden ingredients.
    Exclude containers and packaging.
    Return [] if no food ingredients are visible.
    """

    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=mime_type
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image_part]
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    result = response.text.strip()
    result = re.sub(r"^```(?:json)?\s*", "", result)
    result = re.sub(r"\s*```$", "", result)

    ingredients = json.loads(result)

    if not isinstance(ingredients, list):
        raise ValueError("Invalid ingredient response.")

    return list(dict.fromkeys(
        item.strip().lower()
        for item in ingredients
        if isinstance(item, str) and item.strip()
    ))