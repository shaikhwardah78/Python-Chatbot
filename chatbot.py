def get_reply(user_message):
    message = user_message.lower()
    if "hello" in message or "hi" in message:
        return "Hi Welcome!👋, How can i help you?"
    elif "How are you?" in message:
        return "I'm doing great, thanks for asking! How about you?"
    elif "What is your name?" in message: 
        return "I'm Chatbot 1.0, your new Python friend!"
    elif "OK ,If i want any help then i will ask you. Goodbye! 👋" in message:
        return "Yeah! Ok i will help you anytime. Goodbye! 👋"

print("🤖 Welcome to your first ChatBot!")
print("Type 'bye',If you wan to exit the chatbot.\n")

while True:
    user_input = input("YOU:")

    reply = get_reply(user_input)
    print("Bot:", reply)
    if "bye" in user_input.lower():
        break
print("\n Chat ended. Thanks for chatting!")



