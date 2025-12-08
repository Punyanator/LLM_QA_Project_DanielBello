import re
import os
from google import genai
from dotenv import load_dotenv

# Load local .env for API key (only for local dev)
load_dotenv()

# Read API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found. Please set it in your .env or environment variables.")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Preprocess user input
def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

# Call Gemini API safely
def call_gemini(prompt, model="gemini-2.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text

# Main CLI loop
def main():
    print("=== LLM Q&A CLI (Gemini) ===")
    while True:
        q = input("Question> ").strip()
        if q.lower() in ("exit", "quit"):
            break

        processed = preprocess(q)
        print(f"[Processed]: {processed}")

        try:
            answer = call_gemini(processed)
            print("Answer:", answer)
        except Exception as e:
            print("Error calling Gemini:", e)

if __name__ == "__main__":
    main()
