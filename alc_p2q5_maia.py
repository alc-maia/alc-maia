import numpy as np

def alc_cholesky(A):

    # Verifica se a matriz é quadrada
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("A matriz de entrada deve ser quadrada")
    
    # Cria uma matriz R de zeros com o mesmo tamanho de A
    R = np.zeros((n, n))

    # Itera sobre cada linha da matriz A
    for i in range(n):
        # Calcula o valor temporário (tmp) para o elemento da diagonal
        tmp = A[i, i]
        for j in range(i):
            tmp -= R[j, i] ** 2
        
        # Verifica se o valor temporário é positivo
        if tmp <= 0:
            raise Exception("A matriz não é positiva definida")

        # Define o valor do elemento da diagonal de R
        R[i, i] = np.sqrt(tmp)
        
        # Itera sobre os elementos acima da diagonal para atualizar a matriz R
        for j in range(i + 1, n):
            # Calcula o valor do elemento R[i, j]
            soma = 0
            for k in range(i):
                soma += R[k, i] * R[k, j]
            R[i, j] = (A[i, j] - soma) / R[i, i]
    
    return R
