import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Define some example responses
responses = {
    "greet": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day!",
    "name": "I'm a chatbot created using spaCy.",
    "do": "How do you do?",
    "default": "I'm sorry, I didn't understand that. Can you rephrase?"
}

# Define some keywords and corresponding intents
intents = {
    "hello": "greet",
    "hi": "greet",
    "hey": "greet",
    "bye": "goodbye",
    "goodbye": "goodbye",
    "name": "name",
    "do": "do",
}

def get_intent(doc):
    # Check for keywords in the user's input
    for token in doc:
        if token.text.lower() in intents:
            return intents[token.text.lower()]
    return "default"

def respond(user_input):
    # Process the user input with spaCy
    doc = nlp(user_input)
    # Determine the intent
    intent = get_intent(doc)
    # Fetch the appropriate response
    return responses[intent]

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot:", responses["goodbye"])
        break
    print("Bot:", respond(user_input))