from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return "Hello from kirin-vision-demo using OpenAI Vision!"

@app.route("/analyze", methods=["POST"])
def analyze():
    image_url = request.json.get("image_url")
    if not image_url:
        return jsonify({"error": "image_url is required"}), 400

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "あなたは画像から情報を読み取り、分かりやすく説明するアシスタントです。"},
            {"role": "user", "content": f"以下の画像を見てください: {image_url}"}
        ],
        max_tokens=500
    )
    result = response.choices[0].message.content
    return jsonify({"result": result})
