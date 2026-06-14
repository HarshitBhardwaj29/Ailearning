import numpy as np

# slicing
arr = np.array([1,2,3,4,5,6,7,8])
print('Basic slicing',arr[2:7])
print("With step",arr[1:8:2])
print("Negative",arr[-3])

arr2D = np.array([[1,2,3],[3,4,5]])
print("specific element",arr2D[1,2])
print("entire row",arr2D[1])

# sorting 
unsorted = np.array([4,3,7])
print(np.sort(unsorted))

arr2dunsorted = np.array([[3,1],[1,2],[2,3]])
print("sorted 2d array by column",np.sort(arr2dunsorted,axis=1))


# Filtering 
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_num = numbers[numbers %2==0]
print("even numbers",even_num)


# Filter with mask
mask = numbers>5
print("Numbers greater tahn 5",numbers[mask])


#Fancy indexing vs np.where
indices = [0,2,4]
#take value from numbers array
print[numbers[indices]]

where_result = np.where(numbers>5)
print("NP where",numbers[where_result])

condition_array = np.where(numbers>5)
print(condition_array)


# Adding and removing data
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
combined = arr1+arr2
print(combined)

# array compatibilty
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a.shape == b.shape)

original = np.array([[1,2],[3,4]])
new_row = np.array([[5,6]])

with_new_row = np.vstack((original,new_row))
new_col = np.array([[7],[8]])
with_new_col = np.hstack((original,new_col))

# deleting
arr = np.array([1,2,3,4,5])
deleted = np.delete(arr,2)
print(deleted)