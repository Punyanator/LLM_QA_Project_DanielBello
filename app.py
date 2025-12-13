from flask import Flask, render_template, request
import os
import re
from google import genai
import time
from google.genai.errors import ClientError

app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)





def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def call_gemini(prompt, model="gemini-2.5-flash"):
    resp = client.models.generate_content(model=model, contents=prompt)
    return resp.text

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    processed = None
    question = None

    if request.method == "POST":
        question = request.form.get("question", "")
        processed = preprocess(question)
        answer = call_gemini(processed)

    return render_template("index.html", question=question, processed=processed, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
