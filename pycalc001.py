import os

class Calculator:
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while True:
            self.clear_screen()

            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                result = self.calculate(num1, op, num2)
                print(f"Result: {result}")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            if input("Would you like to continue? (y/n): ").lower() != 'y':
                self.clear_screen()
                break

    def calculate(self, num1, op, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        else:
            return "Invalid operator"


if __name__ == "__main__":
    calc = Calculator()
    calc.run()