import re
from google import genai

# Preprocess
def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

# Use the Gemini API key directly


def call_gemini(prompt, model="gemini-2.5-flash"):
    resp = client.models.generate_content(model=model, contents=prompt)
    return resp.text

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
