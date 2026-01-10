import numpy as np
# arr1=np.array([1,2,3])#1-D array
# print(arr1)
# print(type(arr1))
# print(arr1.shape)


# arr2=np.array([1,2,3,4,5])
# arr2 =arr2.reshape(1,5)#reshaping to 1 row and 5 coloumn
# # arr3=np.array([[1,2,3,4,5]])#Used list inside a list
# print(arr2.shape)

# arr3=np.array([[1,2,3,4,5],[2,3,4,5,6]])
# print(arr3)
# print(arr3.shape)#returns 2 rows and 5 coloums
# arr6=np.arange(0,10,2)#2 is skip step parameter
# arr7=np.arange(0,12,2).reshape(2,3)#reshape into 5 row and 1 coloum
# print(arr6)
# print(arr7)


# np.ones((3,4))
# np.eye(3)
# arr = np.array([[1,2,3],[4,5,6]])

# print("Array:", arr)
# print("Shape:", arr.shape)
# print("Number of dimension:", arr.ndim)
# print("Size(number of elements):", arr.size)
# print("Data type:", arr.dtype)
# print("Item size(in bytes):", arr.itemsize)



# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([10,20,30,40,50])

# #Element-wise operations
# print("Addition:", arr1+arr2)
# print("Substraction:", arr1-arr2)
# print("Multiplication:", arr1*arr2)
# print("Division:", arr1/arr2)


# arr = np.array([10,20,30,40,50])

# print(np.sqrt(arr))
# print(np.exp(arr))
# print(np.sin(arr))
# print(np.log(arr))


# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("Array: \n",arr)
# print(arr[0][0]) #1
# print(arr[2][1]) #10

# print(arr[1:,2:])# [row 1 to empty means last row , coloum 2 to empty means last coloum] 
# print(arr[0:2,2:])#[row 0 to row 2(means row before 2= 1), coloum 2 to empty means last coloum]
# print(arr[1:,1:3])


# arr[0][0]=100
# print(arr)#element at index 0,0 will be replaced by 100

# arr[1:]=100
# print(arr)#all the element from row 1 to last row which is row 2 will be replaced by 100


# #To have a mean of 0 and standard deviation of 1
# data = np.array([1,2,3,4,5])

# #Calculating mean and standard deviation
# mean = np.mean(data)
# std_dev = np.std(data)

# #Normalize the data 
# normalized_data = (data - mean) / std_dev
# print("Normalized data:", normalized_data)

# data = np.array([1,2,3,4,5,6,7,8,9])

# #Mean
# mean = np.mean(data)
# print("Mean:", mean)

# #Median
# median = np.median(data)
# print("Median:", median)

# #Standard deviation 
# std_dev = np.std(data)
# print("Standard deviation:", std_dev)

# #Variance
# variance = np.var(data)
# print("Variance:", variance)


# data = np.array([1,2,3,4,5,6,7,8,9])

# print(data>5) #return boolean output
# print(data[data>5]) #return which elements are greater then 5

# print(data[(data>=5) & (data<=8)])
# print(data[(data<3) | (data>7)])








#Question 1
arr = np.arange(10,51)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

#Question 2
arr1 = np.arange(1,17).reshape(4,4)
print(arr1)
print(arr1[3,2])
print(arr1[2:])


#Question 3 
a=np.array([2, 4, 6, 8])
b=np.array([1, 3, 5, 7])
print("Add:",a+b)
print("Mul:",a*b)
print("Div:",a/b)


#Question 4
arr2 = np.arange(0,21)
print(arr2[(arr2 > 10) & (arr2 <= 18)])


