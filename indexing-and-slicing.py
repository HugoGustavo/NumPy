import numpy as np

a = np.arange(10)
s = slice(2,7,2)
print(a[s])

a = np.arange(10)
b = a[2:7:2]
print(b)

a = np.arange(10)
b = a[5]
print(b)

a = np.arange(10)
print(a[2:])

a = np.arange(10)
print(a[2:5])

a = np.array([
    [1,2,3],
    [3,4,5],
    [4,5,6]
])
print(a)

print('Now we will slice the array form the index a[1:]')
print(a[1:])

a = np.array([
    [1,2,3],
    [3,4,5],
    [4,5,6]
])
print('Our array is: ')
print(a)
print('\n')

print('The item items in the second row are: ')
print(a[1,...])
print('\n')

print('The items columns 1 onwards are: ')
print(a[..., 1:])