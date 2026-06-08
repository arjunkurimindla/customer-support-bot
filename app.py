from flask import Flask, request, jsonify, render_template
import json
import random
import mysql.connector

app = Flask(__name__)

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_support"
)

cursor = conn.cursor()

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)


# Chatbot Response Function
def get_response(message):

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in message.lower():

                return random.choice(
                    intent["responses"]
                )

    return "Sorry, I didn't understand."


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data["message"]

    return jsonify({
        "reply": get_response(message)
    })


# Order Tracking API
@app.route("/order/<order_id>")
def track_order(order_id):

    cursor.execute(
        "SELECT status FROM orders WHERE order_id=%s",
        (order_id.upper(),)
    )

    result = cursor.fetchone()

    if result:
        return jsonify({
            "order_id": order_id.upper(),
            "status": result[0]
        })

    return jsonify({
        "error": "Order not found"
    })


if __name__ == "__main__":
    app.run(debug=True)