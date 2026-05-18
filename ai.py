def chatbot():
    print("Hi, I'm DivyaBot. Ask me about my skills!")
    while True:
        user = input("You: ").lower()
        if "python" in user:
            print("Bot: I completed Python for Data Science from IIT Madras. I built Library Management System using Python.")
        elif "salary" in user or "expectation" in user:
            print("Bot: I'm looking for industry standards for freshers, around 18K-25K. Growth matters more to me.")
        elif "night shift" in user:
            print("Bot: Yes, I'm open to night shifts and ready to join immediately.")
        elif "bye" in user:
            print("Bot: Thanks! Hope to work with your team.")
            break
        else:
            print("Bot: I have skills in Python, SQL basics, Excel. Ask me about projects!")

chatbot()