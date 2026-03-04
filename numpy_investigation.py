# numpy_investigation.py

import numpy as np


arr = np.array([1, 2, 3])

print (arr)

m1 = np.random.randint(1, 10, (4, 4))
m2 = np.random.randint(1, 10, (4, 4))

print (m1)
print (m2)

print (m1 + m2)

print (m1 * 2)

print (m1 * m2)


print (m1.shape)

m1 = m1.reshape((2, 8))

print (m1)

print (m1.reshape((8,2)))
print (m1.reshape((1,16)))

rns = np.random.randint(1, 100, 100)

print (rns)

ones = np.zeros((5,5))
print (ones)

arr = np.array(range(1, 17)).reshape((4,4))

print (arr)

# extra slicing options

# slice rows using this
print (arr[1:3])

# slice column index 2 
print (arr[:,2:3])

# slice a section
print (arr[2:,2:])






