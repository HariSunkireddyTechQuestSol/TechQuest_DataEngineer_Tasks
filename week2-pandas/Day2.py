import pandas as pd 

x = pd.Series([10,20,1,32,9,15,32,12,76])
print(x)
print("Min: ",x.min())
print("Mean: ",x.mean())
print("Max: ",x.max())


data = {
    "name":["Jane", "Smith", "Jake", "Jack", "Rohit","Shimbu","Vidya"],
    "age":[23,25,27,25,34,45,20],
    "city":["Hyd","Vizag","Kadapa","Hyd","Bangalore","TamilNadu",""],
    "Designation":["Doctor", "Cricketer", "Politician", "Doctor","Singer","Actor",""]
}

#creating a dataframe 
df = pd.DataFrame(data)

print(df)

#Accessig columns 

print(df.name)
print(df.age)
print(df.city)
print(df.Designation)

df.to_csv("Sample.CSV")