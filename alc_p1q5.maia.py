# -*- coding: utf-8 -*-
"""
@author: bryan
"""

# 5ª Questão (2,0pt)

import numpy as np

def inversa_eliminacao(A):
   
    # Verifica se a matriz é quadrada

    linhas, colunas = A.shape[0], A.shape[1]
    if linhas != colunas:
        raise ValueError("A matriz deve ser quadrada.")
    n = linhas  # Número de linhas (ou colunas) da matriz
    
    # Verifica elementos nulos na diagonal principal
    for i in range(n):
        if A[i, i] == 0:
            raise ValueError("A matriz possui elementos nulos na diagonal principal. Use outra função para calcular a inversa.")

    # Cria a matriz identidade de tamanho n x n
    I = np.eye(n)
    
    # Cria a matriz aumentada (A | I)
    AI = np.zeros((n, 2 * n))  # Matriz aumentada com n linhas e 2n colunas
    for i in range(n):
        for j in range(n):
            AI[i, j] = A[i, j]  # Lado esquerdo da matriz (A)
        for j in range(n):
            AI[i, j + n] = I[i, j]  # Lado direito da matriz (identidade)
    
    print("Matriz aumentada inicial (A | I):")
    print(AI)  # Printa a matriz aumentada no início dos tempos

    # Aplica o método de eliminação de Gauss-Jordan
    for i in range(n):
        print(f"\nOperações na linha {i+1}:") # Começo a contar da linha 1 até a linha n
        pivo = AI[i, i]  # Elemento da diagonal principal da i-ésima linha
        print(f"Elemento da diagonal principal: {pivo}")
        for j in range(2 * n):
            AI[i, j] /= pivo  # Divide todos os elementos da i-ésima linha pelo elemento da diagonal principal
        print(f"Matriz após dividir a linha {i+1} pelo elemento da diagonal principal:")
        print(AI)  # Printa a matriz aumentada após dividir a linha i pelo pivô

        for k in range(n):
            if i != k:  # Se a linha i não for igual à linha k
                print(f"Eliminando o elemento da coluna {i+1}, linha {k+1}:")
                pivo = AI[k, i]
                print(f"Fazendo L{k+1} = L{k+1} - L{i+1} * (L{k+1, i} / L{i+1, i})") # Operações para zerar os elementos abaixo do pivô
                for j in range(2 * n):
                    # Subtrai de todos os elementos da k-ésima linha o produto do elemento da k-ésima linha com o elemento da i-ésima linha
                    AI[k, j] -= pivo * AI[i, j]
                # O objetivo é fazer com que todos os elementos na coluna da posição i, exceto o pivô, sejam zero. 
                # Para isso, subtraímos uma fração da linha atual da linha k. 
                # Esta fração é calculada multiplicando o valor da célula pivô da linha k pela linha i. 
                # O resultado é subtraído da linha k para eliminar o valor na coluna i.
                print(f"Matriz após eliminação na linha {k+1}:")
                print(AI)
    
    # A inversa está na parte direita da matriz aumentada
    inv_A = np.zeros((n, n))  # Matriz de zeros com n linhas e n colunas
    for i in range(n):
        for j in range(n):
            inv_A[i, j] = AI[i, j + n]  # Preenche a matriz inversa com os valores da parte direita da matriz aumentada
    
    return inv_A


# Teste da função usando diferentes matrizes
    # Teste 1: Matriz 2x2
A = np.array([[1, 2], [3, 4]])
print("Matriz A:")
print(A)
try:
    inv_A = inversa_eliminacao(A)
    print("Matriz inversa de A:")
    print(inv_A)
except ValueError as e:
    print(e)

# Teste 2: Matriz 3x3
B = np.array([[2, -1, 0], [1, 2, -1], [3, 0, 1]])
print("\nMatriz B:")
print(B)
try:
    inv_B = inversa_eliminacao(B)
    print("Matriz inversa de B:")
    print(inv_B)
except ValueError as e:
    print(e)

# Teste 3: Matriz com zero na diagonal principal
C = np.array([[0, 2], [3, 4]])
print("\nMatriz C:")
print(C)
try:
    inv_C = inversa_eliminacao(C)
    print("Matriz inversa de C:")
    print(inv_C)
except ValueError as e:
    print(e)

# Teste 4: Matriz não quadrada
D = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatriz D:")
print(D)
try:
    inv_D = inversa_eliminacao(D)
    print("Matriz inversa de D:")
    print(inv_D)
except ValueError as e:
    print(e)

# Teste 5: Matriz identidade 3x3
E = np.eye(3)
print("\nMatriz E (Identidade):")
print(E)
try:
    inv_E = inversa_eliminacao(E)
    print("Matriz inversa de E:")
    print(inv_E)
except ValueError as e:
    print(e)
