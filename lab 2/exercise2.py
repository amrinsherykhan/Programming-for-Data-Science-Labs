#  Exercise 2

#7
students = [
    {"name": "Raha", "department": "CSE", "marks": 85},
    {"name": "Karima", "department": "CSE", "marks": 48},
    {"name": "Sara", "department": "DS", "marks": 91},
    {"name": "Nadia", "department": "DS", "marks": 67},
    {"name": "Hasnim", "department": "CSE", "marks": 73}
]

total = 0
highest_student = students[0]

for student in students:
    total += student["marks"]

    if student["marks"] > highest_student["marks"]:
        highest_student = student

average = total / len(students)

passed = 0

for student in students:
    if student["marks"] >= 50:
        passed += 1

print("Total students:", len(students))
print("Average marks:", average)
print("Number of students who passed:", passed)

print(
    "Highest-scoring student:",
    highest_student["name"],
    "-",
    highest_student["marks"]
)
#5
products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0

for product in products:
    cost = product["price"] * product["quantity"]
    total += cost

    print(product["name"], "Cost:", cost)


def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total


final_total = apply_discount(total)

print("Original total:", total)
print("Final total:", final_total)

#6
number = int(input("Enter a non-negative integer: "))

while number < 0:
    print("Please enter a non-negative integer.")
    number = int(input("Enter a non-negative integer: "))

while number >= 0:
    print(number)
    number -= 1


    


 