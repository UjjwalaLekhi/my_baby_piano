from google import genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)


def get_song_notes(song_name):

    prompt = f"""
You are a music note extraction assistant.

The user wants the main melody notes for:
"{song_name}"

Return ONLY valid JSON.

Format:

{{
    "song": "name",
    "tempo": 120,
    "notes": [
        {{
            "note": "C4",
            "duration": 500
        }},
        {{
            "note": "D4",
            "duration": 500
        }}
    ]
}}

Rules:
- Notes must use scientific pitch notation (C4, D#4, etc.)
- Duration is in milliseconds
- Only return JSON
- Do not add explanations
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text

    # Remove markdown if Gemini adds ```json
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        data = json.loads(text)
        return data

    except json.JSONDecodeError:
        print("Gemini returned invalid JSON:")
        print(text)
        return None
