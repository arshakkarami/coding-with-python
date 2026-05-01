name = str(input("What is your name: "))
last_name = str(input("What is your Last name: "))
age = int(input("Ho old are you? "))


print(f"Hi im {name} {last_name}  and im {age}.")

if age >= 18:
    print(f"{name} are you good to sing.")
else:
    print(f"surry {name} you can't sing.")
