import json
import random
import mysql.connector

with open("intents.json", "r") as file:
    data = json.load(file)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_support"
)

cursor = conn.cursor()

print("Customer Support Bot Started")
print("Type 'quit' to exit")

while True:

    user_input = input("You: ").lower()

    if user_input == "quit":
        break

    found = False

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in user_input:

                print(
                    "Bot:",
                    random.choice(intent["responses"])
                )

                if intent["tag"] == "order_status":

                    order_id = input(
                        "Order ID: "
                    ).upper()

                    cursor.execute(
                        "SELECT status FROM orders WHERE order_id=%s",
                        (order_id,)
                    )

                    result = cursor.fetchone()

                    if result:
                        print(
                            "Bot: Your order status is",
                            result[0]
                        )
                    else:
                        print(
                            "Bot: Order not found"
                        )

                found = True
                break

        if found:
            break

    if not found:
        print(
            "Bot: Sorry, didn't get that!"
        )

conn.close()