from flask import Flask, request, jsonify, render_template
from groq import Groq
import os 

app = Flask(__name__)
client=Groq(
    api_key=("YOUR_GROQ_API_KE"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run(debug=True)