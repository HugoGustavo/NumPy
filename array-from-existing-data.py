import numpy as np

x = [1, 2, 3]
a = np.asarray(x)
print(a)

x = [1, 2, 3]
a = np.asarray(x, dtype = float)
print(a)

x = (1, 2, 3)
a = np.asarray(x)
print(a)

x = [(1,2,3), (4,5)]
a = np.asarray(x)
print(a)

#s = 'Hello World'
#a = np.frombuffer(
#    s,
#    dtype = 'S1'
#)
# print(a)

lista = range(5)
print(lista)

lista = range(5)
it = iter(lista)
x = np.fromiter(it, dtype = float)
print(x)
