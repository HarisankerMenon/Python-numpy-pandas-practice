#  2 dimensional array

import numpy as np
a=np.array(([1,2,3],[4,5,6]))    # order :- [2,3]
print(a)

print(a.ndim)

#..........................................

# 2 dimension array create [4*3] metrix

import numpy as np
b=np.array(([1,2,3,],[4,5,6,],[7,8,9,],[10,11,12]))    # order :- [4,3]
print(b)

print(b.ndim)

#............................................

# 3 dimensional array matrix [3,3]


import numpy as np
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])                # order :- [3,3]
print(c)

print(c.ndim)


# 3 dimensional array matrix [4*3]


import numpy as np
d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])     # order :- [4,3]
print(d)

print(d.ndim)


#.............................................

# shape  :- order of array or metrix
# ----------------------------------

import numpy as np
e=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])     # order :- [4,3]
print(e)

print(e.ndim)

# shape:-

print(e.shape)

#...............................................


import numpy as np
f=np.array(([1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13],[13,14,15,16]))    # order :- [5,4]
print(f)

print(f.ndim)

print(f.shape)


import numpy as np
d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])     # order :- [4,3]
print(d)

print(d.ndim)

# shape of 3 dimensional array  [1,4,3]  :- [z,x,y]

#..............................................................

# shape of 1 dimensional array


import numpy as np

a=np.array([1,2,3,4,5])

print(a)

print(a.ndim)

print(a.shape)




