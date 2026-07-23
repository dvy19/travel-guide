from google import genai
from django.conf import settings
import json

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def recommend_places(mood):

    prompt = f"""
    The user is travelling in Kanpur.

    Their mood is {mood}.

    Recommend exactly 5 places.

    Return ONLY valid JSON.

    Example:

    [
      {{
        "name":"JK Temple",
        "reason":"Peaceful atmosphere"
      }}
    ]
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print(response.text)

    return json.loads(response.text)