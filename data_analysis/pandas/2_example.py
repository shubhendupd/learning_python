# Cleaning data

# Remove rows that contain empty cell using dropna

import pandas as pd
'''
df = pd.read_csv('dataset_files\\workout_data.csv')

new_df = df.dropna()

print(new_df.to_string())
'''
# dropna method will return a new dataframe and doesnt change the original 
# to change the original mention inplace = True
'''
df.dropna(inplace=True)
print(df.to_string())
'''
# filena method allows to replace empty cell with some value.
'''
df = pd.read_csv('dataset_files\\workout_data.csv')
df.fillna({'Calories' : 99}, inplace=True)
print(df.to_string())
'''
# fillna method is not suitable for mixed dataset so for that we have to guid fillna 
# where to put data at which coloumn

df = pd.read_csv("dataset_files\\workout_data.csv")
'''
fill_values = {}

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(99)
    else:
        df[col] = df[col].fillna('99')


print(df.to_string())
'''
# Calculate mean , median and mode[0]
'''
x = df["Calories"].mean()

df.fillna({'Calories' : x}, inplace= True)
print(df.to_string())

print(x)

'''

#todatetime() method
'''
df["Date"] = pd.to_datetime(df["Date"], format = 'mixed')
#print(df.to_string())

df.dropna(subset=['Date'], inplace =True)

print(df.to_string())

'''
#Replace value

df.loc[7,'Duration'] = 45
print(df.to_string())

#loop through all value in the "duration" column
#if value is higher than 120 set it to 120.

for x in df.index:
    if df.loc[x,"Duration"] > 50:
        df.loc[x, "Duration"] = 50

print(df.to_string())