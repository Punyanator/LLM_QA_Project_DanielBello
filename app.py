from flask import Flask, render_template, request
import re
from google import genai
import os
app = Flask(__name__)

import os
api_key = os.environ["AI_API_KEY"]

# Preprocess function
def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

# Gemini client (use your actual key here or environment variable)
client = genai.Client(api_key="AIzaSyDUYUH6-X6Rrv3RkEkY6GYgldBOXilyzMY")  # <-- put your key

# Function to call Gemini
def call_gemini(prompt, model="gemini-2.5-flash"):
    resp = client.models.generate_content(model=model, contents=prompt)
    return resp.text

@app.route("/", methods=["GET", "POST"])
def index():
    question = None
    processed = None
    answer = None

    if request.method == "POST":
        question = request.form.get("question", "")
        processed = preprocess(question)
        try:
            answer = call_gemini(processed)
        except Exception as e:
            answer = f"Error calling Gemini: {e}"

    return render_template("index.html", question=question, processed=processed, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
