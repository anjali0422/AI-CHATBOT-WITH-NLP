import nltk
from nltk.chat.util import Chat, reflections

# Sample pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"hi|hello",
        ["Hello!", "Hi there!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer simple questions."]
    ],
    [
        r"bye",
        ["Goodbye!", "Have a nice day!"]
    ],
]

# Create chatbot
def start_chat():
    print("Hi, I'm your AI chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chat()
