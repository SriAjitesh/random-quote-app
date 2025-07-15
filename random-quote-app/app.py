from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Simplicity is the ultimate sophistication.",
    "Dream big. Start small. Act now.",
    "You miss 100% of the shots you don’t take."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
