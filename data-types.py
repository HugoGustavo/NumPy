import numpy as np

dt = np.dtype(np.int32)
print(dt)

dt = np.dtype('i8')
print(dt)

dt = np.dtype('>i2')
print(dt)

dt = np.dtype([
    ('age', np.int8)
])
print(dt)

dt = np.dtype([
    ('age', np.int8)
])
a = np.array([
    (10,),
    (20,),
    (30,)
], dtype = dt)
print(a)

dt = np.dtype([
    ('age', np.int8)
])
a = np.array([
    (10,),
    (20,),
    (30,)
], dtype = dt)
print(a['age'])

student = np.dtype([
    ('name', 'S20'),
    ('age', 'i1'),
    ('marks', 'f4')
])
print(student)

student = np.dtype([
    ('name', 'S20'),
    ('age', 'i1'),
    ('marks', 'f4')
])
a = np.array([
    ('abc', 21, 50),
    ('xyz', 29, 75)
], dtype=student)
print(a)