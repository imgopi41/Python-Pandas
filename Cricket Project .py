import pandas as pd
import numpy as np

a = pd.read_csv(r'C:\Users\admin\Desktop\Gopinath\My Excel Files\2023 Ipl.csv')     #Reading a CSV file
# print(a)

# print(a.head(5))                      #Printing first five Rows
# print(a.tail(5))                      #Printing last five Rows

# print(a[4:9])                         #Printing Random rows csv file
# print(a.info())                       #Displays Information from your dataframe

# print(a.describe())                   #Describes Statistical Values

# print(a.columns)                      #Displaying Columns by Columns Function (method 1) of displaying columns
# print(list(a.columns))                #Displaying Columns by using List (method 2) of displaying columns
# print(a.loc[[],:])                    #Displaying Columns by using .loc Method (method 3) of displaying columns

# for i in a.columns:                   #Displaying Columns by using for loop (method 4) of displaying columns
    # print(i)

# print(a.groupby(['Color']).size())    #Grouping By Color and Displaying by Size

# print(a.isnull().sum())               #Checking for null Value if null (1) is displayed if not(0) to be printed
# print(a.isnull().values.any())        #Checking for null Value if null True is displayed if not False to be printed





