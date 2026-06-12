import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array)
print(type(array))
print(array.shape)

arr2D = np.array([[1,2,3],[1,2,3]])
print(arr2D)


list = [1,2,4]
print(list*2)

ny_array = np.array([1,2,3])
print(ny_array*2)


zeros = np.zeros((3,4))
print(zeros)

ones = np.ones((3,4))
print(ones)


full = np.full((2,2),7)
print(full)

random = np.random.random((2,3))
print(random)

sequence = np.arange(0,10,2)
print(sequence)


vector = np.array([1,2,3])
print(vector)

matrix = np.array([[1,2,3],[4,5,6]])

tensor = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# Array Properties
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)

#Array Reshaping
arr1 = np.arange(12)
print(arr1)
reshaped = arr1.reshape((3,4))
print(reshaped)

flattened = reshaped.flatten()
print(flattened)

raveled = reshaped.ravel()
print(raveled)

#Transpose of matrix
transpose = reshaped.T
print(transpose)