def chatbot():
    print("Chatbot: Hello! I am a rule-based chatbot.")
    print("Chatbot: Type 'bye'  to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day ")
            break

        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: Hi there! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm fine! Thanks for asking.")

        elif "your name" in user_input:
            print("Chatbot: My name name is chitti.")
        elif "what can you do" in user_input:
            print("Chatbot: I can answer basic questions and chat with you.")

        elif "help" in user_input:
            print("Chatbot: I can answer simple questions like greetings and help messages.")
            
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
