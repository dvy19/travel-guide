from google import genai
from django.conf import settings
import json
import traceback

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def recommend_places(mood):
    try:
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
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )

        print("========== GEMINI RESPONSE ==========")
        print(response)
        print("=====================================")

        response_text = response.text
        print("Response Text:", response_text)

        try:
            return json.loads(response_text)

        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            print("Raw Response:", response_text)
            traceback.print_exc()
            raise

    except Exception as e:
        print("Gemini API Error:", str(e))
        traceback.print_exc()
        raise