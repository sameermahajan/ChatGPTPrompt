# pip install flask openai python-dotenv
# export OPENAI_API_KEY="your_api_key_here"
#    or
# setx OPENAI_API_KEY "your_api_key_here"

import os
from flask import Flask, request, jsonify
from openai import OpenAI
from flask import render_template

# -----------------------------
# Configuration
# -----------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

# -----------------------------
# Health check
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# -----------------------------
# Main query endpoint
# -----------------------------
@app.route("/query", methods=["POST"])
def query():
    data = request.get_json(silent=True)
    if not data or "query" not in data:
        return jsonify({"error": "Missing 'query' field"}), 400

    user_query = data["query"]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7
        )

        answer = response.choices[0].message.content

        return jsonify({
            "query": user_query,
            "answer": answer
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    # 0.0.0.0 makes it accessible remotely
    app.run(host="0.0.0.0", port=5000, debug=False)
