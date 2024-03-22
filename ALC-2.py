# -*- coding: utf-8 -*-
"""
@author: bryan
"""
import numpy as np
def sub_reg(A,b):
    x = np.zeros((len(A),1))
    lin = len(A)
    #lin, col = A.shape
    for i in range(lin-1,-1,-1):
        x[i] = (b[i] - sum(A[i][j]*x[j] for j in range(i,lin)))/A[i][i]
    return x

A = np.array([[1,2],
              [0,3]])
b = np.array([[2],[5]])

# colunas é len(A[0])

x = sub_reg(A,b)
print(x)
