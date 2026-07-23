import google.generativeai as genai
from django.conf import settings
import json
from rest_framework.response import Response
import traceback

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def recommend_places(mood):
    try:
        prompt = f"""
        The user is travelling in Kanpur.

        Their mood is {mood}.

        Recommend exactly five places.

        Return ONLY valid JSON.
        """

        response = model.generate_content(prompt)

        print("Gemini Response:")
        print(response.text)

        return response.text

    except Exception as e:
        print("ERROR OCCURRED:")
        traceback.print_exc()
        raise