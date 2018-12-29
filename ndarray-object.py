import numpy as np
a = np.array(
    [1,2,3]
)

print (a)

# mais de uma dimensao
a = np.array([
    [1,2],
    [3,4]
])

print(a)

# menor dimensao
a = np.array(
    [1,2,3,4,5],
    ndmin = 2
)
print(a)

# parametro dtype

a = np.array(
    [1,2,3],
    dtype = complex
)

print (a)