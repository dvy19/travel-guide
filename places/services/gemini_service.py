import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def recommend_places(mood):
    prompt = f"""
    The user is travelling in Kanpur.

    Their mood is {mood}.

    Recommend exactly five places.

    Return ONLY JSON.

    Example:

    [
      {{
        "name":"JK Temple",
        "reason":"Peaceful atmosphere",
      }}
    ]
    """

    response = model.generate_content(prompt)

    text = response.text

    return json.loads(text)