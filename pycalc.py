import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calc_main():
    while True:
        clear_screen()

        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print(num1 + num2)
            elif op == "*":
                print(num1 * num2)
            elif op == '-':
                print(num1 - num2)
            elif op == "/":
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(num1 / num2)
            else:
                print("Invalid operator")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

        if input("Would you like to Continue? (y/n): ").lower() != 'y':
            clear_screen()
            break

if __name__ == "__main__":
    calc_main()