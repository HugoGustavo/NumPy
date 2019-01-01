import numpy as np

print('Concatenate two strings: ')
print(np.char.add(['hello'], ['xyz']))
print('\n')
print('Concatenation example: ')
print(np.char.add(['hello', 'hi'], ['abc', 'xyz']))

print(np.char.multiply('Hello ', 3))

print(np.char.center('hello', 20, fillchar='*'))

print(np.char.capitalize('hello world'))

print(np.char.title('hello, how are you?'))

print(np.char.lower(['HELLO', 'WORLD']))

print(np.char.lower('HELLO'))

print(np.char.upper('hello'))
print(np.char.upper(['hello', 'world']))

print(np.char.split('hello how are you?'))
print(np.char.split('TutorialsPoint,Hyderabad,Telangana', sep=','))

print(np.char.splitlines('hello\nhow are you?'))
print(np.char.splitlines('hello\rhow are you?'))

print(np.char.strip('ashok arora', 'a'))
print(np.char.strip(['arora', 'admin', 'java'], 'a'))

print(np.char.join(':', 'dmy'))
print(np.char.join([':','-'], ['dmy', 'ymd']))

print(np.char.replace('He is a good boy', 'is', 'was'))

a = np.char.encode('hello', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))