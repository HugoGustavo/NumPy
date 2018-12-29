import numpy as np

a = np.arange(8)
print('The original array: ')
print(a)
print('\n')
b = a.reshape(4,2)
print('The modified array: ')
print(b)

a = np.arange(8).reshape(2,4)
print('The original array: ')
print(a)
print('\n')
print('After applying the flating function: ')
print(a.flat[5])

a = np.arange(8).reshape(2,4)
print('The original array is:')
print(a)
print('The flattened array is: ')
print(a.flatten())
print('\n')
print('The flattened array in F-style ordering:')
print(a.flatten(order='F'))

a = np.arange(8).reshape(2,4)
print('The original array is: ')
print(a)
print('\n')
print('After applying ravel function: ')
print(a.ravel())
print('\n')
print('Applying ravel function in F-style ordering: ')
print(a.ravel(order='F'))

a = np.arange(12).reshape(3,4)
print('The original array is: ')
print(a)
print('\n')
print('The transposed array is: ')
print(np.transpose(a))

a=np.arange(12).reshape(3,4)
print('The original array is: ')
print(a)
print('\n')
print('Array after applying the function: ')
print(a.T)

a = np.arange(8).reshape(2,2,2)
print('The original array: ')
print(a)
print('\n')
print('The array after applying the swapaxes function: ')
print(np.swapaxes(a,2,0))

x = np.array([
    [1],
    [2],
    [3]
])
y = np.array([
    4,
    5,
    6
])
b = np.broadcast(x,y)
#print('Broadcast x against y: ')
#(r,c) = b.iters
#print(r.next(), c.next())
#print(r.next(), c.next())
print('\n')
print('The shape of broadcast object: ')
print(b.shape)
print('\n')
b = np.broadcast(x,y)
c = np.empty(b.shape)
print('Add x and y manually using broadcast: ')
print(c.shape)
print('\n')
c.flat = [ u+v for (u,v) in b ]
print('After playing the flat function: ')
print(c)
print('\n')
print('The summation of x and y: ')
print(x + y)

a = np.arange(4).reshape(1,4)
print('The original array: ')
print(a)
print('\n')
print('After applying the broadcast_to function: ')
print(np.broadcast_to(a, (4,4)))

a = np.arange(4).reshape(1,4)
print('The original array: ')
print(a)
print('\n')
print('After applying the broadcast_to function: ')
print(np.broadcast_to(a, (4,4)))

x = np.array((
    [1,2],
    [3,4]
))
print('Array x: ')
print(x)
print('\n')
y = np.expand_dims(x, axis = 0)
print('Array y: ')
print(y)
print('\n')
print('The shape of X and Y array: ')
print(x.shape, y.shape)
print('\n')
y = np.expand_dims(x, axis=1)
print('Array Y after inserting axis at position 1: ')
print(y)
print('\n')
print('x.ndim and y.ndim')
print(x.ndim, y.ndim)
print('\n')
print('x.shape and y.shape')
print(x.shape, y.shape)

x = np.arange(9).reshape(1,3,3)
print('Array X: ')
print(x)
print('\n')
y = np.squeeze(x)
print('Array Y: ')
print(y)
print('\n')
print('The shapes of X and Y array: ')
print(x.shape, y.shape)

a = np.array([
    [1,2],
    [3,4]
])
print('First array: ')
print(a)
print('\n')
b = np.array([
    [5,6],
    [7,8]
])
print('Second array: ')
print(b)
print('\n')
print('Joining the two arrays along axis 0: ')
print(np.concatenate((a,b)))
print('\n')
print('Joining the two arrays along axis 1: ')
print(np.concatenate((a,b), axis=1))

a = np.array([
    [1,2],
    [3,4]
])
print('\nFirst Array: ')
print(a)
print('\n')
b = np.array([
    [5,6],
    [7,8]
])
print('Second Array: ')
print(b)
print('\n')
print('Stack the two arrays along axis 0: ')
print(np.stack((a,b), 0))
print('\n')
print('Stack the two arrays along axis 1: ')
print(np.stack((a,b), 1))

a = np.array([
    [1,2],
    [3,4]
])
print ('\nFirst array: ')
print(a)
print('\n')
b = np.array([
    [5,6],
    [7,8]
])
print('Second array: ')
print(b)
print('\n')
print('Horizontal stacking: ')
c = np.hstack((a,b))
print(c)
print('\n')

a = np.array([
    [1,2],
    [3,4]
])
print('First array: ')
print(a)
print('\n')
b = np.array([
    [5,6],
    [7,8]
])
print('Second array: ')
print(b)
print('\n')
print('Vertical stacking: ')
c = np.vstack((a,b))
print(c)

a = np.arange(9)
print('First array: ')
print(a)
print('\n')
print('Split the array in 3 equal-sized subarrays: ')
b = np.split(a, 3)
print(b)
print('\n')
print('Split the array at positions indicated in 1-D array: ')
b = np.split(a, [4,7])
print(b)

a = np.arange(16).reshape(4,4)
print('First array: ')
print(a)
print('\n')
print('Horizontal splitting: ')
b = np.hsplit(a,2)
print(b)
print('\n')

a = np.arange(16).reshape(4,4)
print('First array: ')
print(a)
print('\n')
print('Vertical splitting: ')
b = np.vsplit(a, 2)
print(b)

a = np.array([
    [1,2,3],
    [4,5,6]
])
print('First array: ')
print(a)
print('\n')
print('The shape of first array: ')
print(a.shape)
print('\n')
b = np.resize(a, (3,2))
print('Second array: ')
print(b)
print('\n')
print('The shape of second array: ')
print(b.shape)
print('\n')
print('Resize the second array: ')
b = np.resize(a, (3,3))
print(b)

a = np.array([
    [1,2,3],
    [4,5,6]
])
print('First array: ')
print(a)
print('\n')
print('Append elements to array: ')
print(np.append(a, [7,8,9]))
print('\n')
print('Append elements along axis 0: ')
print(np.append(a, [[7,8,9]], axis=0))
print('\n')
print('Append elements along axis 1: ')
print(np.append(a, [[5,5,5],[7,8,9]], axis=1))

a = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print('First array: ')
print(a)
print('\n')
print('Axis parameter not passed. The input array is flattened before insertion.')
print(np.insert(a, 3, [11,12]))
print('\n')
print('Axis parameter not passed. The values array is broadcast to match input array.')
print('Broadcast along axis 0: ')
print(np.insert(a, 1, [11], axis=0))
print('\n')
print('Broadcast along axis 1: ')
print(np.insert(a, 1, 11, axis=1))

a = np.arange(12).reshape(3,4)
print('\nFirst array: ')
print(a)
print('\n')
print('Array flattened begore delete operation as axis not used: ')
print(np.delete(a, 5))
print('\n')
print('Column 2 deleted: ')
print(np.delete(a, 1, axis=1))
print('\n')
print('A slice containing alternate values from array deleted: ')
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.delete(a, np.s_[::2]))

a = np.array([5,2,6,2,7,5,6,8,2,9])
print('\nFirst array: ')
print(a)
print('\n')
print('Unique values of first array: ')
u = np.unique(a)
print(u)
print('\n')
print('Unique array and Indices array: ')
(u, indices) = np.unique(a, return_index=True)
print(indices)
print('\n')
print('We can see each number corresponds to index in original array: ')
print(a)
print('\n')
print('Indices of unique array: ')
(u, indices) = np.unique(a, return_inverse=True)
print(u)
print('\n')
print('Indices are: ')
print(indices)
print('\n')
print('Reconstruct the original array using indices: ')
print(u[indices])
print('\n')
print('Return the count of repetitions of unique elements: ')
(u, indices) = np.unique(a, return_counts=True)
print(indices)