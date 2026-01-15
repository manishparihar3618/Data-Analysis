# import pandas as pd
# data=[1,2,3,4,5]
# series = pd.Series(data)
# print(series)
# data = {'a':1,'b':2,'c':3}
# series=pd.Series(data)
# print(series)#keys will be considered as index and values will be considered as series values
# data=[10,20,30,40]
# index=['a','b','c','d'] 
# pd.Series(data,index) 
# data ={ 
# 'Name':['Manish','Joan','Jason','Vladimir'],
# 'Age':['18','24','26','55'],
# 'City':['Indore','Barcelona','Londan','Moscow']
# }
# index =['a','b','c','d']     
# df=pd.DataFrame(data,index) 
# print(df) 
# print(type(df)) 
# data1 =[
# {'Name':'Manish','Age':18,'City':'Indore'},
# {'Name':'Joan','Age':24,'City':'Barcelona'},
# {'Name':'Jason','Age':26,'City':'London'},
# {'Name':'Vladimir','Age':55,'City':'Moscow'},
# ]
# df1=pd.DataFrame(data1)
# print(df1)
# print(type(df1))
# sales_df=pd.read_csv('sales_csv.csv')
# sales_df
# sales_df=pd.read_csv('sales_csv.csv')
# sales_df.head(5)#head(5)We will get first or top 5 entries
# sales_df.tail(5)#tail(5) will give us last 5 entries
# ### Accessing Data from DataFrame
# sales_df
# sales_df['Product']#Will print all Product or We have accessed Series Product from DataFrames sales_df.
# sales_df.loc[0]#We can access Row using loc method
# print(sales_df.loc[0, 'Product'])   
# print(sales_df.loc[0, 'Quantity'])
# #We can also use iloc to access rows and columns by their integer position
# #Used to access elements by position using row and coloumn numbers
# sales_df.iloc[0]
# print(sales_df.iloc[0, 2])   
# print(sales_df.iloc[5, 1])
# #Accessing a specified element
# sales_df.at[1,'Date']#From Row which is 1 take Date or[Row index,column name]
# #Accessing specified element using iat
# sales_df.iat[2,2]#[Row index,column,index]
# sales_df['Discount(in %)']=[5,5,10,5,10,5,10,10,10,5]
# sales_df
# # sales_df.drop('Discount(in %)')
# # # KeyError occurs because drop() removes rows by default (axis=0).
# # # Pandas looks for 'Discount(in %)' in the ROW NAMES on the left side.
# # # But 'Discount(in %)' is written at the TOP of the table (it is a column).
# # # Since no row has this name, pandas raises a KeyError.
# sales_df.drop('Discount(in %)',axis=1)
# # Now, we specified axis=1, so pandas looks for 'Discount(in %)' in the COLUMN NAMES at the TOP of the table.
# # It finds it and removes the entire column.
# sales_df
# #Now we can see that the original DataFrame is unchanged.
# #This is because, by default, drop() returns a new DataFrame with the specified labels removed.
# sales_df.drop('Discount(in %)', axis=1, inplace=True)
# #Now, the original DataFrame is changed because we used inplace=True.     
# #Now we will increase the Price of all products by 10%
# sales_df['Price']=sales_df['Price']*1.1
# sales_df
# sales_df.drop(0,inplace=True)
# #Statistical summary
# sales_df.describe()
# #Return data types of each column
# print(sales_df.dtypes)
# student_df=pd.read_csv('student_data.csv')
# student_df
# #Check for missing values
# student_df.isnull()
# # this will return a DataFrame of the same shape as student_df, with True indicating missing values and False indicating non-missing values.
# student_df.isnull().any()
# # this will return a Series with column names as index and boolean values indicating whether each column contains any missing values.
# # for example, if the 'Age' column has any missing values, the corresponding value in the Series will be True; otherwise, it will be False.
# student_df.isnull().sum()
# # This will give the count of missing values in each column of the student_df DataFrame.
# # student_df.fillna(0)
# # This will replace all missing values (NaN) in the student_df DataFrame with 0.
# student_df['Attendance_fillNA']=student_df['Attendance'].fillna(student_df['Attendance'].mean())
# # This will create a new column 'Attendance_fillNA' in the student_df DataFrame, where all missing values in the 'Attendance' column are replaced with the mean value of the 'Attendance' column.
# student_df
# student_df = student_df.rename(columns ={'Name':'Student Name'})
# #We can rename the column using this rename method and we have to permanatly store in student_df
# # Now 'Name' column is renamed to 'Student Name' Permanatly
# student_df.head()
# student_df['Age(int)'] = student_df['Age'].astype(int)
# student_df.head()
# # Here we have converted the 'Age' column from its current data type to integer using the astype(int) method.
# # If there were any non-integer values in the 'Age' column, this operation would raise an error.
# # We we have a Nan value in MathScore column then while converting to int it will raise an error.
# # Here we will use the fillna() method to handle missing values before converting the column to integer.
# student_df['MathScore_fillNA(int)'] = student_df['MathScore'].fillna(student_df['MathScore'].mean()).astype(int)
# student_df.head()
# student_df['New_ScienceScore'] = student_df['ScienceScore'].apply(lambda x: x + 5)
# student_df.head()
# # Here we have used the apply() method along with a lambda function to add 5 to each value in the 'ScienceScore' column.
# grouped_by_city = student_df.groupby('City')['MathScore'].mean()
# print(grouped_by_city)
# # Here we have grouped the DataFrame by the 'City' column and calculated the mean of the 'MathScore' for each city using the groupby() method.
# grouped_sum_by_city = student_df.groupby('City')['ScienceScore'].sum()
# print(grouped_sum_by_city)
# # Here we have grouped the DataFrame by the 'City' column and calculated the sum of the 'ScienceScore' for each city using the groupby() method.
# # aggregate multiple functions
# grouped_agg= student_df.groupby('City')['Age'].agg(['mean','sum','max'])
# print(grouped_agg)
# # Here we have grouped the DataFrame by the 'City' column and applied multiple aggregation functions (mean, sum, max) on the 'Age' column using the agg() method.
# # Sample DataFrame
# data1= pd.DataFrame({'Key': ['A', 'B', 'C', 'D'],'Value1': [10, 20, 30, 40]})
# data2= pd.DataFrame({'Key': ['A', 'B', 'C', 'E'],'Value2': [100, 200, 300, 400]})
# data1
# data2
# # Merge DataFrames on 'Key' column
# pd.merge(data1, data2, on='Key', how='inner')
# # We gave parameter data1 and data2 on which the merge will be performed and 'Key' is the common column on which we are merging and how='inner' means only the common keys will be considered in the merged DataFrame.
# # on='Key' means on key column the merge will be performed.
# # how='inner' means only the common keys will be considered in the merged DataFrame.
# pd.merge(data1, data2, on='Key', how='outer')
# # We gave parameter data1 and data2 on which the merge will be performed and 'Key' is the common column on which we are merging and how='outer' means all keys from both DataFrames will be included in the merged DataFrame.
# # on='Key' means on key column the merge will be performed.
# # how='outer' means all keys from both DataFrames will be included in the merged DataFrame.
# pd.merge(data1, data2, on='Key', how='left')
# #how='left' means all keys from the left DataFrame (data1) will be included in the merged DataFrame, and only matching keys from the right DataFrame (data2) will be merged.
# pd.merge(data1, data2, on='Key', how='right')
# #how='right' means all keys from the right DataFrame (data2) will be included in the merged DataFrame, and only matching keys from the left DataFrame (data1) will be merged.
# import pandas as pd 
# from io import StringIO
# Data = '[{"Name": "Manish", "Age": "18", "City": "Indore", "Country": "India"}]'
# # Converting JSON to DataFrame
# data_df = pd.read_json(StringIO(Data))
# data_df
# # Coverting DataFrame back to JSON
# data_df.to_json()
# # We have got the JSON representation of the DataFrame data_df.
# data_df.to_json(orient='index')
# # We have got the JSON representation of the DataFrame data_df in 'index' orientation.
# # This means that the JSON object will be structured with the DataFrame's index as the outermost keys, and each key will map to another JSON object representing the corresponding row of data.
# # Now we will save this DataFrame to a local CSV file
# url_df.to_csv("wine.csv")
# # This will save the DataFrame url_df to a CSV file named "wine.csv" in the current working directory.
# # Reading data from HTML files
# html_df = pd.read_html("https://www.fdic.gov/bank/individual/failed/banklist.html")    
# html_df
# url = "https://en.wikipedia.org/wiki/Mobile_country_code"
# pd.read_html(url)
# pd.read_excel('Book1.xlsx', sheet_name='Sheet1')
# # We can read Excel files using pandas' read_excel function.
# # sheet_name='Sheet1' specifies that we want to read the data from the sheet named 'Sheet1' in the Excel file.
# # By default, read_excel reads the first sheet if sheet_name is not specified.
# df_excel = pd.read_excel('Book1.xlsx')
# #Pickle in Python is primarily used for serializing and deserializing Python object structures. In other words, it allows you to convert a Python object into a byte stream (serialization) to store it in a file/database, maintain program state across sessions, or transport data over a network, and then later reconstruct the original object from that byte stream (deserialization).
# df_excel.to_pickle('excel_data.pkl')










































# # Loading the pickled DataFrame
# # df_from_pickle = pd.read_pickle('excel_data.pkl')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
import numpy as np

# #Assignment 1 
# #Question 1
# arr1 = np.arange(0,50,2).reshape(5,5)
# print(arr1)

# #Question 2
# arr2 =np.arange(1,17).reshape(4,4)
# arr2[0][0]=0
# arr2[1][1]=0
# arr2[2][2]=0
# arr2[3][3]=0
# print(arr2)


# #Assignment 2
# arr3 = np.arange(1,37).reshape(6,6)
# print(arr3)
# print(arr3[2:5,1:4])

# arr4 = np.arange(1,26).reshape(5,5)
# print(arr4)
# # # print(arr4[0:,:])


# #Assignment 3
# arr5 = np.arange(0,12).reshape(3,4)
# arr6 = np.arange(13,25).reshape(3,4)
# print(arr5+arr6)
# #same *-/ can be performed 

# arr7 =np.arange(1,17).reshape(4,4)



data = np.arange(1,26).reshape(5,5)
mean = np.mean(data)
median = np.median(data)
std= np.std(data)
var=np.var(data)
print(mean)
print(median)
print(std)
print(var)



data = np.arange(0,9).reshape(3,3)
mean = np.mean(data)
std_dev = np.std(data)
#Normalize the data 
normalized_data = (data - mean) / std_dev
print(normalized_data)














































































