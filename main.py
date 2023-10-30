import nltk
from nltk.chat.util import Chat, reflections
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

def is_response_empty(response):
    # Check if the response is empty or contains only whitespace characters
    return not response.strip()
def main():
    chatbot = initialize_chatbot("database.txt")
    print("Hello! I'm your chatbot. Type 'quit' or 'exit' to end the conversation.")
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
