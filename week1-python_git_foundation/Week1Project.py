# Week 1 Project 

# Taking user input 

name = input("Please enter user name: ")
age = int(input("Please enter age: "))
salary = float(input("Salary: "))

# Writing the employee information to the CSV file and reading content from that CSV file

with open("Employee.csv","w+") as f:
    f.write(f'Name: {name}, Age: {age}, Salary: {salary}')
    f.seek(0)
    content = f.read()
    print(content)

