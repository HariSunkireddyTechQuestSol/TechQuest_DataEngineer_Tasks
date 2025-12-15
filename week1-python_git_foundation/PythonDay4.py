# File Handling in Python 

# Writing Content to an text file 

with open("SampleFile.txt","w") as f:
    f.write("Animal is very interesting! First thing first, this is my own file i can write anything except this.. hahaha.. \n \nEnd of the topic")
    print("Content has been written to file successfully. ")

# Reading the content from the text file  

with open("SampleFile.txt","r") as f:
    content = f.read()
    print(content)

# Exception handling - Trying to read a file which doesn't exist

try: 
    with open("None.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print(" File you are trying to read does not exist !",e)
