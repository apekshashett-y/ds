def course_chatbot():
    print("Bot: Hello! Welcome to CodeAcademy Online. What's your name?")
    name = input("You: ")
    print(f"Bot: Hi {name}! How can I help you today?")
    print("  1. View available courses\n  2. Course pricing\n  3. Enroll in a course\n  4. Talk to support\n  5. Exit")

    while True:
        choice = input("You (enter 1-5): ").strip()
        if choice == "1":
            print("Bot: We offer these courses:")
            print("   • Python Basics\n   • Web Development (HTML/CSS/JS)\n   • Data Science with Python\n   • Java Programming")
            print("Bot: Anything else? (1-5)")

        elif choice == "2":
            print("Bot: Course prices:")
            print("   • Python Basics – $49")
            print("   • Web Development – $79")
            print("   • Data Science – $99")
            print("   • Java Programming – $69")
            print("Bot: Anything else? (1-5)")

        elif choice == "3":
            print("Bot: Which course would you like to enroll in? (enter name exactly)")
            course = input("You: ")
            print(f"Bot: Great choice! You've been enrolled in '{course}'.")
            print("Bot: A confirmation email will arrive shortly. Anything else? (1-5)")

        elif choice == "4":
            print("Bot: Our support email is support@codeacademy.com. Anything else? (1-5)")

        elif choice == "5":
            print(f"Bot: Thanks for visiting, {name}! Happy coding. Goodbye!")
            break

        else:
            print("Bot: Sorry, I didn’t get that. Please enter 1, 2, 3, 4 or 5.")


course_chatbot()