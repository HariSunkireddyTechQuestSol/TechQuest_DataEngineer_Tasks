import pandas as pd 
import numpy as np

print("Pandas Version: ",pd.__version__)
print("Numpy Version: ",np.__version__)

#Initializing array x
x = np.array([10, 20, 30, 40])
print ("array1: ",x)

#Initializing array y
y = np.array([1, 2, 3, 4])
print("array2: ",y)

print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** 2)
