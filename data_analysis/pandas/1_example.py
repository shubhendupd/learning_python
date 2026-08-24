import pandas as pd
import os
print("Learning Introduction")
print( f" panda version is  {pd.__version__}")

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3, 7, 2]
}

print(type(mydataset))

myvar = pd.DataFrame(mydataset)

print(myvar)
#------------------------------------------------

print("\n Working on Series") # put data in colomn in table

a = [1,7,2]


myvar = pd.Series(a, index = ["x","y","z"]) # Here X y z are label  by default the index start from 0,1,2..
# label is used to access specific value
print(myvar)
print(myvar["y"])

print(myvar.tolist())        # Output: [1, 7, 2]
# or
print(myvar.values)          # Output: [1 7 2]
# or loop through:
for val in myvar:
    print(val)

# Next example
print("---Next example---")

calories = {"day1" :420 , # here key becomes the label
            "day2": 380,
            "day3":390
            }
myvar = pd.Series(calories, index = ["day1","day2"])

print(myvar)
print("value is ", myvar["day2"])

# Moving to learn dataframe
print("\n Learning Dataframe") # mult-dimensional table 

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40 , 45]
}

myvar = pd.DataFrame(data)

print(myvar)

# to locate row we use loc
print("\n")
print("locating row", myvar.loc[1])
print("\n")
print(myvar.loc[[1,2]])

# Naming the indexes
print("\n")
print("Learning to name index \n")

myvar = pd.DataFrame(data, index = ["day1", "day2","day3"])
print(myvar)

print("\n")
print("Locate named index \n", myvar.loc[["day1", "day2"]])


# To load file into dataframe

df = pd.read_csv('data.csv')
print("\n")
print(df)
print("\n")
print(df.to_string())
print("\n")

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999 
print("\n")
print(pd.options.display.max_rows)
# this line will update the max rows pandas display normally if it is having more than 60 then pandas
#will display 5 top and 5 below dataframe.

# reading Json file
print("\n")
print("Learning reading json file")
print(os.listdir("dataset_files"))
df = pd.read_json("dataset_files\\data.json")
print(df.to_string())


# To view the data in pandas use head() method by default it will return top5 

print(df.head(10).to_string())

# To view the data from the last use tail() method by default 5
print("\n")
print(df.tail().to_string())


# to get he information about your data set use info()
print("\n")
print(df.info())