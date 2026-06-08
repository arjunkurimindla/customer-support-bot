Phase 1: Basic Rule-Based Chatbot

    Start simple before adding AI.

    Folder Structure: 
            customer_support_bot/
            │
            ├── bot.py
            ├── intents.json
            ├── requirements.txt
            └── README.md

    Step 1: Create intents.json
    Step 2: Create bot.py

    python bot.py


Phase 2: Add NLP

    pip install nltk ----- Instead of exact matching    (all can be understood.
                Tokenization
                Stemming
                Bag of Words)



Phase 3: Train a Machine Learning Model

    --pip install scikit-learn


                    User Message
                        ↓
                    Vectorization
                        ↓
                    Classification Model
                        ↓
                    Intent Prediction
                        ↓
                    Response


    Example intents:

        Greeting
        Refund
        Return Policy
        Order Status
        Payment Issue
        Technical Support

        Algorithms:

        Naive Bayes
        Logistic Regression
        Random Forest


Phase 4: Store Customer Data

    -Create a database(customer_support) in    workbench 
     -   create a table(orders) with colms 
                       order_id
                       customer_name
                       product_name
                       status
    -    insert values

   - create a file(database.py) in project folder
   - connect it with database
           


