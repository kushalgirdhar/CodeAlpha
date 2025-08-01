# Step 1: Define the chatbot response logic in a function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

# Step 2: Chat loop
print("🤖 Chatbot is ready! (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if user_input.lower() == "bye":
        break
