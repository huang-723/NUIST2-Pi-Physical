# NAME: Huang Yufan
# ID: 20119455
# Date: 2026-03-30
# NUIST Python Quiz Game with GPIO LED feedback, green for correct, red for incorrect
import RPi.GPIO as GPIO
import time
GREEN_LED = 17
RED_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(GREEN_LED, GPIO.LOW)
GPIO.output(RED_LED, GPIO.LOW)
def python_quiz():
    print("Welcome to the Python Quiz!")
    print("Answer with the option letter (a/b/c/d/e), e.g., a\n")
    questions = [
        "1. Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool\nYour answer: ",
        "2. Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()\nYour answer: ",
        "3. In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats\nYour answer: ",
        "4. The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try\nYour answer: ",
        "5. What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break\nYour answer: "
    ]
    correct_answers = ["c", "d", "d", "c", "d"]
    score = 0

    for i in range(len(questions)):
        user_ans = input(questions[i]).strip().lower()
        if user_ans == correct_answers[i]:
            print(f"Correct! The answer is {correct_answers[i]} - Green LED on")
            score += 1

            GPIO.output(GREEN_LED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(GREEN_LED, GPIO.LOW)
        else:
            print(f"Incorrect! Correct answer is {correct_answers[i]} - Red LED on")

            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(RED_LED, GPIO.LOW)
        print("-"*30, "\n")
    print("\nQuiz Completed!")
    print(f"You got {score}/{len(questions)} questions correct.")
    GPIO.cleanup()

if __name__ == "__main__":
    python_quiz()
