import numpy as np
from scipy.linalg import lu

def lu_decomposition(A):
    # Decomposição LU usando eliminação gaussiana com pivoteamento parcial.
    n = A.shape[0]
    L = np.eye(n)  # Matriz triangular inferior inicialmente como matriz identidade
    U = A.copy()  # Matriz triangular superior inicialmente como uma cópia de A
    P = np.eye(n)  # Matriz de permutação inicialmente como matriz identidade
    
    for i in range(n):
        # Encontrar o índice do maior elemento na coluna i
        pivot_index = np.argmax(np.abs(U[i:, i])) + i
        if i != pivot_index:
            # Trocar linhas i e pivot_index em U
            U[[i, pivot_index]] = U[[pivot_index, i]]
            # Trocar linhas i e pivot_index em P
            P[[i, pivot_index]] = P[[pivot_index, i]]
            # Trocar linhas i e pivot_index em L, mas somente as colunas 0 até i-1
            if i > 0:
                L[[i, pivot_index], :i] = L[[pivot_index, i], :i]
        
        # Calcular os multiplicadores
        for j in range(i+1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] -= L[j, i] * U[i, i:]
            U[j, i] = 0  # Atribuir 0 para assegurar a triangularidade inferior de U
    
    return P, L, U

# Teste do algoritmo
A = np.array([[2, -1, -2],
              [-4, 6, 3],
              [-4, -2, 8]], dtype=float)

P, L, U = lu_decomposition(A)

print("Matriz A:")
print(A)
print("\nMatriz de Permutação P:")
print(P)
print("\nMatriz Triangular Inferior L:")
print(L)
print("\nMatriz Triangular Superior U:")
print(U)

# Verificação usando scipy.linalg.lu
P_scipy, L_scipy, U_scipy = lu(A)

print("\nComparação com scipy.linalg.lu:")
print("P_scipy:")
print(P_scipy)
print("L_scipy:")
print(L_scipy)
print("U_scipy:")
print(U_scipy)
