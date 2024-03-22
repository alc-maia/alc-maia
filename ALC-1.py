# -*- coding: utf-8 -*-

# Produto de matrizes

import numpy as np
"""
A = np.array ([[1,-1,2],[0,2,1],[2,3,1]])

print(A)

B = np.array ([[1,1],[-1,-3],[2,0.5]])

print (B)

C= A @ B

C

A = np.array([[1,1],[1,0]])

for i in range(5):
    print(np.linalg.matrix_power(A,i))
    
E = np.array([[5,3],[3,2]])

np.linalg.inv(E)

np.matrix.transpose(A)

A = np.array([[1,1,-1],[2,1,1],[-1,-2,3]])
Ainv = (np.linalg.inv(A))
print(Ainv)
b = np.matrix.transpose(np.array([[2,0,4]]))

x = Ainv @ b

print(x)

"""
A = np.array([[2,1,3],[1,1,2],[0,2,0]])
Ainv = (np.linalg.inv(A))

print(Ainv)

"""