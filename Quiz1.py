# NUIST Animal Quiz Game in Python3
# NAME: Huang Yufan
# ID: 20119455
# DATE: 2026-3-30
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions (enter the full name in lowercase):")
    questions = [
        "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat\nYour answer: ",
        "2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird\nYour answer: ",
        "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin\nYour answer: "
    ]
    answers = [
        "blue whale",
        "hummingbird",
        "bat"
    ]
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")
quiz()
