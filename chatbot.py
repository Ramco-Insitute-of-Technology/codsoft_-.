import random
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "default": "I'm sorry, I didn't quite understand that. How can I assist you?"
}
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return responses[key]
    return responses["default"]
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
