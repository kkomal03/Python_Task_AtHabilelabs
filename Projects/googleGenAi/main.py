import base64
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
def generate():
    user_question = input("What do you want to ask releted to domain ? ")

  
    domain = "cooking"

  
    prompt = f"""
You are an expert assistant only allowed to answer questions in the domain of {domain}.
If the user's question is related to {domain}, give a helpful answer.
If it is outside the domain of {domain}, respond only with: "This question is outside your domain."
User's question: {user_question}
"""

   
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

  
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]


    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model="gemini-2.5-flash-lite",
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


if __name__ == "__main__":
    generate()
