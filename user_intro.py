# Taking user input

name = input("Enter your name: ")
age = int(input("Enter your age: "))   # Type casting to integer
city = input("Enter your city: ")

# Displaying a formatted introduction

print("\n----- Introduction -----")
print("Hello! My name is", name)
print("I am", age, "years old.")
print("I live in", city + ".")
print("------------------------")