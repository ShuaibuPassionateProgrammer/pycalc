#Simple python prgram that demonstrate the use of calculator
num1 = float(input("Enter first number: "))
operator = input("Enter a valid operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
	print(num1 + num2)
elif operator == "*":
	print(num1 * num2)
elif operator == "-":
	print(num1 - num2)
elif operator == "/":
	if num2 == 0:
		print("Cannot divide by zero")
	else: 
		print(num1 / num2)
else:
	print("Invalid operator")

if input("Enter any value to exit, or press enter to continue: "):
	break
