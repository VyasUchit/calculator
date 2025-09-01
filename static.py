import pyttsx3
import datetime 
HISTORY_FILE = "history.txt"

# Initialize the speech engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

    # Speak out loud

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def say_and_print(text):
    print(text)
    speak(text)
    
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    say_and_print(f"{greeting} Welcome to the simple calculator.")
    
    
def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
        if not lines:
            say_and_print("No history found.")
        else:
            say_and_print("History of calculations:")
        for line in reversed(lines):
            say_and_print(line.strip())
    except FileNotFoundError:
        say_and_print("No history file found.")
    
def clear_history():
    with open(HISTORY_FILE, "w"):
        pass
    say_and_print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")
    
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        say_and_print("Invalid input format. Please use: <number1> <operator> <number2>")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "**":
        result = num1 ** num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            say_and_print("Error: Division by zero is not allowed.")
            return
    else:
        say_and_print("Invalid operator. USE ONLY +, -, *, / or **")
        return

    if int(result) == result:
        result = int(result)
        say_and_print(f"Result is: {result}")
    save_to_history(user_input, result)

 # greet user based on time of day
    
def main():
    
    wish_me()
    while True:
        user_input = input("Enter calculation (+,-,*,/,**) or command (history,clear,exit): ")
        if user_input == "exit":
            say_and_print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)
                 
main() 