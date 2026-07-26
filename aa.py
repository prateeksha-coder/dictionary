student = { "name": "Alice", "age": 20, "course": "Python"}

print(student)
print("Name:", student["name"])
print("Age:", student.get("age"))

student["marks"] = 95
print(student)

removed = student.pop("marks")
print(student)

print("\nIterating Through Dictionary:")
for key, value in student.items():
    print(key, ":->", value)

student.clear()
print(student)
