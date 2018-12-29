import numpy as np

x = np.array([
    [1,2],
    [3,4],
    [5,6]
])
y = x [
    [0,1,2],
    [0,1,0]
]
print(y)

x = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9,10,11]
])
print('Our array is: ', x, '\n')
rows = np.array([
    [0,0],
    [3,3]
])
cols = np.array([
    [0,2],
    [0,2]
])
y = x[rows, cols]
print(y)

x = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9,10,11]
])
print('Our array is', x, '\n')
z = x[1:4, 1:3]
print('After slicing, our array becomes: ', z, '\n')

y = x[1:4, [1,2]]
print('Slicinng using advanced index for column: ', y, '\n')

x = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
])
print('Our array is', x, '\n')
print ('The items greater than 5 are: ', x[x>5])

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])