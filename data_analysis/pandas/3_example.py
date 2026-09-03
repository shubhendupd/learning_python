#correlation 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_files\\data_3.csv")

#print(df.corr())
#corr method ignore non numeric coloumns

#df.plot()

#plt.show()

# Scatter plot kind show x and y

#df.plot(kind = 'scatter', x ='Duration', y = 'Calories')

#plt.show()


#histrogram show frequecy at each interval and we need only one coloumn

df['Calories'].plot(kind='hist')
plt.show()