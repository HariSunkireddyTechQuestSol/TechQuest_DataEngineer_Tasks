# ----------------------------------------------
#Lists and Dictionaries Practice

# 1️ Create a list of 10 numbers
numbers = [10, 23, 45, 66, 78, 89, 90, 33, 42, 17]

print("Even Numbers in the list:")

# Looping through each number and check if even
for num in numbers:
    if num % 2 == 0:
        print(num)

# ----------------------------------------------

# 2️ To Store employee details in a dictionary
employee = {
    "name": "Hari Sunki Reddy",
    "age": 26,
    "department": "Data Engineering",
    "salary": 75000,
    "location": "Ohio, USA"
}

print("\nEmployee Details:")
# Printing all key-value pairs
for key, value in employee.items():
    print(f"{key} : {value}")


