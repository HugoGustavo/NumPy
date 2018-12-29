import numpy as np

x = np.arange(5)
print(x)

x = np.arange(5, dtype = float)
print(x)

x = np.arange(10,20,2)
print(x)

x = np.linspace(10,20,5)
print(x)

x = np.linspace(10,20,5, endpoint=False)
print(x)

x = np.linspace(1,2,5, retstep=True)
print(x)

a = np.logspace(1.0, 2.0, num=10)
print(a)

a = np.logspace(1,10, num=10, base=2)
print(a)