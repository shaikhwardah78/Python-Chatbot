# I used def function (to decides what reply to give based on what the user said)
# This is main chatting part for btw you and bot 
def get_reply(user_message):
    message = user_message.lower()
    if "hello" in message or "hi" in message:
        return "Hi Welcome!👋, How can i help you?"
    elif "how are you?" in message:
        return "I'm doing great, thanks for asking! How about you?"
    elif "what is your name?" in message: 
        return "I'm Chatbot 1.0, your new Python friend!"
    elif "ok if i want any help then i will ask you. goodbye!" in message:
        return "Yeah! Ok i will help you anytime. Goodbye!👋"

print("-"*40)
print("🤖 Welcome to your first ChatBot!")
print("-"*40)
print("Type 'bye',If you want to exit the chatbot.\n")

# This the loop part for chat end (I used while loop) and also input() function.
while True:
    user_input = input("YOU:")

    reply = get_reply(user_input)
    print("Bot:", reply)
    if "bye" in user_input.lower():
        break
print("\n Chat ended. Thanks for chatting!")



