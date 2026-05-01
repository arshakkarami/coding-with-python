weight = float(input("Enter your weight:"))
unit = input("Kilograms or punds? (K or L): ")

if unit == "K":
weight = weight * 2.205
unit = "Lbs."
print(f"You weight is: {round(weight,1)} {unit}")
elif unit == "L":
weight = weight / 2.205
unit = "kgs."
print(f"You weight is: {round(weight,1)} {unit}")
else:
print(f"{unit} was not valid")
