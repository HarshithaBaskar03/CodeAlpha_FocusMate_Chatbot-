import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def chatbot():
    slow_print("🤖 Welcome to FOCUSMATE!")
    name = input("Enter your name: ")

    slow_print(f"\nHey {name}! I'm FocusMate 💜")
    slow_print("Your personal study companion created by Harshitha ✨")

    while True:
        print("\n===== FOCUSMATE MENU =====")
        print("1. Study Booster Tips")
        print("2. Cheer Me Up")
        print("3. Feeling Lazy 😴")
        print("4. Set My Study Goal")
        print("5. Quick Break Idea")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            slow_print("📚 Tip: Study in 25 min sessions + 5 min breaks!")
            slow_print("Keep distractions away and stay focused 🔥")

        elif choice == "2":
            slow_print("💫 Hey! You’re doing better than you think.")
            slow_print("Don’t give up now — success is close 💪")

        elif choice == "3":
            slow_print("😅 Feeling lazy ah?")
            slow_print("Just start with 5 minutes… that’s enough to begin!")

        elif choice == "4":
            goal = input("How many hours will you study today? ")
            slow_print(f"🔥 Nice {name}! Let’s aim for {goal} hours today!")
            slow_print("Small steps → Big success 💯")

        elif choice == "5":
            slow_print("🌿 Take a short walk or drink water!")
            slow_print("Refresh and come back stronger ⚡")

        elif choice == "6":
            slow_print(f"Goodbye {name}! Proud of you 💖 Keep shining 🌟")
            break

        else:
            slow_print("❌ Oops! Invalid option, try again.")

chatbot()