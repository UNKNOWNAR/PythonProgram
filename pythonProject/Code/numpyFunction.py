import numpy as np

# 1. Creating Arrays
# Single-dimensional array
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

# Multi-dimensional array
arr2 = np.array([[1, 2], [3, 4]])
print("\n2D Array:\n", arr2)

# Array with specific data type
arr3 = np.array([1, 2, 3], dtype=np.float32)
print("\nArray with float32 dtype:", arr3)

# 2. Array Creation Functions
# Array with zeros
zeros = np.zeros((2, 3))
print("\nArray of zeros:\n", zeros)

# Array with ones
ones = np.ones((3, 2))
print("\nArray of ones:\n", ones)

# Identity matrix
identity = np.eye(3)
print("\nIdentity Matrix:\n", identity)

# Array with evenly spaced values (linspace)
linspace = np.linspace(0, 10, 5)
print("\nLinearly spaced array:", linspace)

# Array with range and step size (arange)
arange = np.arange(0, 10, 2)
print("\nArray with range (arange):", arange)

# 3. Random Array Generation
random_array = np.random.random((2, 3))
print("\nRandom array:\n", random_array)

# 4. Array Operations
# Arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nElement-wise addition:", a + b)
print("Element-wise multiplication:", a * b)

# Broadcasting
print("\nBroadcasting example:", a + 5)

# 5. Reshaping and Transposing
reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped array:\n", reshaped)

transposed = reshaped.T
print("\nTransposed array:\n", transposed)

# 6. Indexing and Slicing
# Indexing
print("\nElement at position [1, 2]:", reshaped[1, 2])

# Slicing
print("\nSlicing rows and columns:\n", reshaped[:, 1:3])

# Boolean indexing
print("\nElements greater than 5:", reshaped[reshaped > 5])

# 7. Aggregation and Statistics
print("\nSum of all elements:", reshaped.sum())
print("Mean of all elements:", reshaped.mean())
print("Standard deviation:", reshaped.std())
print("Maximum element:", reshaped.max())
print("Minimum element:", reshaped.min())

# 8. Stacking and Splitting Arrays
# Vertical stacking
stacked = np.vstack((a, b))
print("\nVertically stacked arrays:\n", stacked)

# Horizontal stacking
stacked_horizontal = np.hstack((a.reshape(-1, 1), b.reshape(-1, 1)))
print("\nHorizontally stacked arrays:\n", stacked_horizontal)

# Splitting
arr = np.array([[1,2,6,7],[7,3,10,5]])
split_arrays = np.hsplit(arr, 2)
print("\nSplit arrays (horizontal split):", split_arrays)

# 9. Mathematical Functions
print("\nSine of array elements:", np.sin(a))
print("Exponential of array elements:", np.exp(a))
print("Square root of array elements:", np.sqrt(a))

# 10. Linear Algebra
matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)
print("\nInverse of matrix:\n", inverse)

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

dot_product = np.dot(a, b)
print("\nDot product of two arrays:", dot_product)

# 11. Copying and Views
original = np.array([1, 2, 3])
view = original.view()
copy = original.copy()
view[0] = 100
print("\nOriginal array after modifying view:", original)
print("Copied array remains unchanged:", copy)

# 12. Saving and Loading Arrays
np.save('array.npy', a)  # Save array to file
loaded_array = np.load('array.npy')  # Load array from file
print("\nLoaded array from file:", loaded_array)

#a way to find all numbers greater than five from a bunch of values
arr = np.arange(12).reshape(3,4)
print(arr)
arr1 = arr>5
print(arr1)
print(arr[arr1])