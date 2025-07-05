from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello from kirin-vision-demo!"

if __name__ == "__main__":
    app.run(debug=True)
