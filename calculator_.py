operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if operator == "+":
result = number1 + number2
print(round(result))
elif operator == "-":
result = number1 - number2
print(round(result))
elif operator == "*":
result = number1 * number2
print(round(result))
elif operator == "/":
result = number1 / number2
print(round(result))
else :
print(f"{operator} is not a valid operator")
