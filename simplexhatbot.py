
import re

rules = [
    (r"hello|hi|hey", "Hello! How can I help you?"),
    (r"how are you", "I am fine. Thank you for asking!"),
    (r"what is your name|your name", "My name is SimpleBot."),
    (r"who are you", "I am a simple rule-based chatbot."),
    (r"what can you do|help", "I can answer simple questions."),
    (r"what is artificial intelligence|define ai",
     "AI is the simulation of human intelligence in machines."),
    (r"thank you|thanks", "You are welcome!"),
    (r"bye|goodbye|exit", "Goodbye! Have a nice day.")
]

def chatbot_response(user_input):
    for pattern, response in rules:
        if re.search(pattern, user_input.lower().strip()):
            return response
    return "Sorry, I don't understand that."

print("SIMPLE RULE-BASED CHATBOT")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    print("Bot:", chatbot_response(user_input))
    if re.search(r"bye|goodbye|exit", user_input.lower()):
        break
