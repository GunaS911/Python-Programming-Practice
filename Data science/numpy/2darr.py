import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[1,1])
print(arr[1,:])
print(arr[:,2])
print(arr[0,1:])
print(arr[1:,1:])
arr2=arr[1:,1:]
print(arr2)
