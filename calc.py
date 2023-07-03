print("Enter `+` to add two numbers")
print("Enter `-` to subtract two numbers")
print("Enter `*` to multiply two numbers")
print("Enter `/` to divide two numbers")

user_input = input("Enter your arithmetic function: ")

if user_input in ["+", "-", "*", "/"]:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter another number:"))
    if user_input == "+":
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif user_input == "-":
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif user_input == "*":
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif user_input == "/":
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    print("Invalid input")
