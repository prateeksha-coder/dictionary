student = { "name": "Alice", "age": 20, "course": "Python"}

print("Original Dictionary:")
print(student)

print("\nAccessing Values:")
print("Name:", student["name"])
print("Age:", student.get("age"))

student["marks"] = 95
print(student)

student["age"] = 21
print(student)

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\nIterating Through Dictionary:")
for key, value in student.items():
    print(key, ":->", value)


removed = student.pop("marks")
print("\nRemoved Marks:", removed)
print(student)
 

del student["course"]
print("\nAfter Deleting Course:")
print(student)

student.clear()
print(student)