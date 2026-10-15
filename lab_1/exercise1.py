# Exercise 1


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division is not possible because the second number is zero.")

    celsius = float(input("Enter temperature in Celsius: "))
#2
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", round(fahrenheit, 2))
print("Temperature in Kelvin:", round(kelvin, 2))

#3
name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input("Enter mark for course " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("\n MARKS REPORT ")
print("Student:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Passed courses:", passed)
