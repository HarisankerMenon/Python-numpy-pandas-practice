#   size
#  -------

# size :- total number of element

import numpy as np

a=np.array([1,2,3,4,5])

print(a)

print(a.ndim)

print(a.shape)

print(a.size)

#.........................................................

import numpy as np
b=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])     # order :- [4,3]
print(b)

print(b.ndim)

print(b.shape)

print(b.size)


#  shape = [4*3]= 12 :- size

#............................................................

import numpy as np
c=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])     # order :- [4,3]
print(c)

print(c.ndim)

print(c.shape)

print(c.size)

#..............................................................

import numpy as np
d=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,14]])     # order :- [4,4]
print(d)

print(d.ndim)

print(d.shape)

print(d.size)




























