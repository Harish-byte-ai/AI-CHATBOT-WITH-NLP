import nltk
nltk.download('punkt')        
nltk.download('wordnet')      
nltk.download('omw-1.4')


import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of pattern and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there!"]
    ],
    [
        r"what is your name ?",
        ["I'm CodTech Bot. How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing well!", "All systems go!"]
    ],
    [
        r"what can you do ?",
        ["I can answer basic questions. Try asking me something!"]
    ],
    [
        r"(.*) internship (.*)",
        ["Yes, you'll receive a completion certificate at the end of your internship."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
def start_chat():
    print("Hi, I'm CodTech Bot! Type 'exit' to quit.")
    chatbot.converse()
if __name__ == "__main__":
    start_chat()
