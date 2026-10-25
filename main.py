
from google import genai

# Connect to Google's API
client = genai.Client()

# Ask Gemma 4 a question
response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents="Explain artificial intelligence to a college student."
)

# Display the answer
print(response.text)
