import pandas as pd
import numpy as array
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,('Riti', 30, 'Delhi' , 'India' ),('Vikas', 31, 'Mumbai' , 'India' ),('Neelu', 32, 'Bangalore' , 'India' ),('John', 16, 'New York' , 'US'),('Mike', 17, 'las vegas' , 'US')]
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f'])
print(dfObj)
columnsNamesArr = dfObj.columns.values
print(columnsNamesArr)
print("Get the content from the columns")
listOfColumnNames = list(columnsNamesArr)
print(listOfColumnNames)
print(dfObj.columns.values[2])
indexNamesArr = dfObj.index.values
print(indexNamesArr)
print(len(dfObj['City']))
for i in range(0,len(dfObj['City'])):
       
            print(dfObj['City'].values[i])