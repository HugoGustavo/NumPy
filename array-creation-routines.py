import numpy as np

x = np.empty(
    [3,2],
    dtype = int
)
print(x)

x = np.zeros(5)
print(x)

x = np.zeros(
    (5,),
    dtype = np.int
)
print(x)

x = np.zeros(
    (2,2),
    dtype = [
        ('x', 'i4'),
        ('y', 'i4')
    ]
)
print(x)


x = np.ones(5)
print(x)

x = np.ones(
    [2,2],
    dtype = int
)
print(x)