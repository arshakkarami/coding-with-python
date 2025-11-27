def add (a, b):
    return a + b 

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a % b:
        return "number is 0. "
    return a/b

number1 = float(input("Enter the firast number: "))
operation = input("Enter a operation (-, +, *, %): ")
number2 = float(input("Enter the last number: "))

if operation=="+":
    print(add(number1 ,number2))

elif operation=="-":
    print(add(number1 ,number2))

elif operation=="*":
    print(add(number1 ,number2))

else:
    print(add(number1 ,number2))
