import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)

a = np.array([
    [0.0,   0.0,  0.0],
    [10.0, 10.0, 10.0],
    [20.0, 20.0, 20.0],
    [30.0, 30.0, 30.0]
])
b = np.array([1.0, 2.0, 3.0])
print('First Array\n', a, '\n')
print('Second array\n', b, '\n')
print('First Array + Second Array\n', a+b)