# Exercise 1


marks = [75, 82, 68, 91, 45]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

pass_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Number of students who passed:", pass_count)
#2
temperatures = (28.5, 29.0, 21.2, 27.8, 28.4, 30.1)

for temperature in temperatures:
    print("Temperature:", temperature)

print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))
#3
text = input("Enter a word or short sentence: ")

vowels = 0
spaces = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1

    if character == " ":
        spaces += 1

print("Number of characters:", len(text))
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)

