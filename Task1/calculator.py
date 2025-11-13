# Title: calculator.py
# Author: Vaishnavi Vijayan
# Dis: A friendly, colorful Python CLI calculator with operation history!

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Store operation history
history = []

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return "🚫 Can't divide by zero!" if b == 0 else a / b

def calculator():
    print(Fore.MAGENTA + Style.BRIGHT + "\n✨ Welcome to Vaishnavi's Python Calculator ✨")

    while True:
        print(Fore.CYAN + "\nChoose operation:")
        print("1. Add  2. Subtract  3. Multiply  4. Divide  5. History  6. Exit")

        choice = input(Fore.LIGHTWHITE_EX + "Enter your choice: ").strip()

        if choice == '6':
            print(Fore.LIGHTGREEN_EX + "\nThanks for using the calculator! 💚")
            break

        elif choice == '5':
            print(Fore.YELLOW + "\n📜 History:")
            if not history:
                print("No operations yet!")
            else:
                for record in history:
                    print("•", record)
            continue

        elif choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = add(a, b)
                    symbol = '+'
                elif choice == '2':
                    result = subtract(a, b)
                    symbol = '-'
                elif choice == '3':
                    result = multiply(a, b)
                    symbol = '*'
                elif choice == '4':
                    result = divide(a, b)
                    symbol = '/'

                record = f"{a} {symbol} {b} = {result}"
                history.append(record)
                print(Fore.GREEN + f"Result: {result}")

            except ValueError:
                print(Fore.RED + "⚠️ Please enter valid numbers!")
        else:
            print(Fore.RED + "Invalid choice, try again!")

if __name__ == "__main__":
    calculator()
