# Checking Given Number is positive or negative or zero 

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Printing all the numbers from 1 to 20 using both for and while loops

# Using for loop 

for num in range(1, 21):
    print(num)

# Using while loop

num = 1
while num <= 20:
    print(num)
    num += 1

#Function to add 2 numbers 
#Defining a function 
def add_numbers(a, b):
    return a + b

#calling function 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(add_numbers(num1, num2))