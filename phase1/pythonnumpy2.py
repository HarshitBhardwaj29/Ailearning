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