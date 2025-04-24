responses = {}
print("Hello! I’m your AI assistant.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    if user_input in responses:
        print(f"AI: {responses[user_input]}")
    else:
        response = input("I don’t know that one! What should I say? ")
        responses[user_input] = response
        print(f"AI: {response}")