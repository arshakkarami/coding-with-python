total = 0
marks = int(input("How many tests? "))

for i in range(marks):
mark = float(input("Enter a mark (0 of 100): "))
total += mark

average = total / marks
percent = (average / 100) * 100

print("Average mark: ", average)
print("percent: ",percent, "%")
