import numpy as np

def modgrsch(A):
    # Input: m x n matrix A
    # Output: the QR decomposition A = QR, where
    # Q is an m x n matrix with orthonormal columns, and
    # R is an n x n upper-triangular matrix.
    
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for i in range(n):
        # Q[:, i] = A[:, i]
        Q[:, i] = A[:, i]
        
        for j in range(i):
            # R[j, i] = Q[:, j]' * Q[:, i]
            R[j, i] = np.dot(Q[:, j], Q[:, i])
            
            # Q[:, i] = Q[:, i] - R[j, i] * Q[:, j]
            Q[:, i] = Q[:, i] - R[j, i] * Q[:, j]
        
        # R[i, i] = ||Q[:, i]||
        R[i, i] = np.linalg.norm(Q[:, i])
        
        # Q[:, i] = Q[:, i] / R[i, i]
        Q[:, i] = Q[:, i] / R[i, i]
    
    return Q, R

# Matriz fornecida no exercício 14.15
A = np.array([
    [1, 9, 0, 5, 3, 2],
    [-6, 3, 8, 2, -8, 0],
    [3, 15, 23, 2, 1, 7],
    [3, 57, 35, 1, 7, 9],
    [3, 5, 6, 15, 55, 2],
    [33, 7, 5, 3, 5, 7]
])

# Calculando a decomposição QR usando o algoritmo de Gram-Schmidt modificado
Q_modgrsch, R_modgrsch = modgrsch(A)

print("Q (modgrsch):")
print(Q_modgrsch)
print("\nR (modgrsch):")
print(R_modgrsch)

# Calculando a decomposição QR usando numpy.linalg.qr para comparação
Q_np, R_np = np.linalg.qr(A)

print("\nQ (numpy.linalg.qr):")
print(Q_np)
print("\nR (numpy.linalg.qr):")
print(R_np)

# Comparando os resultados
print("\nDiferença entre Q (modgrsch) e Q (numpy.linalg.qr):")
print(np.abs(Q_modgrsch - Q_np))

print("\nDiferença entre R (modgrsch) e R (numpy.linalg.qr):")
print(np.abs(R_modgrsch - R_np))
