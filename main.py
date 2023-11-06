from nltk.chat.util import Chat, reflections
import sqlite3
from readindatabase import *
conn = sqlite3.connect('therapy.db')
cursor = conn.cursor()
def load_pairs_from_file(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            pattern = lines[i].strip()
            responses = lines[i+1].strip().split('|')
            pairs.append([pattern, responses])
    return pairs

def initialize_chatbot(file_path):
    pairs = load_pairs_from_file(file_path)
    chatbot = Chat(pairs, reflections)
    return chatbot
def main():
    print("Hello! I'm your chatbot. Type 'quit' or 'exit' to end the conversation.")
    generaterecent()
    chatbot = initialize_chatbot("data.txt")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
