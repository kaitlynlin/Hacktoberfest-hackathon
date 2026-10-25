
from google import genai
from google.genai import types

client = genai.Client()

MODEL = "gemma-4-26b-a4b-it"


def ask_gemma(question, image_bytes=None, mime_type=None):
    contents = []

    if image_bytes is not None:
        contents.append(
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            )
        )

    contents.append(question)

    response = client.models.generate_content(
        model=MODEL,
        contents=contents
    )

    return response.text

