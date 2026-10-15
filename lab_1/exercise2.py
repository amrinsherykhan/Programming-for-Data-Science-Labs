# Exercise 2
# Student marks analysis

marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("Total marks:", total)
print("Average marks:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Number of students who passed:", passed)

