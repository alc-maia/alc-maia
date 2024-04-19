# -*- coding: utf-8 -*-
"""
@author: bryan
"""

import numpy as np

# Definindo uma função para realizar o experimento
def realizar_experimento(n):
    # Gerar vetores aleatorios u e v
    u = np.random.rand(n, 1)
    v = np.random.rand(n, 1)
    
    # Calcular a matriz de produto A = uv^T
    A = np.outer(u, v)
    
    # Calcular o posto de A
    posto_A = np.linalg.matrix_rank(A)
    
    # Calcular as normas euclidianas dos vetores u e v
    norma_u = np.linalg.norm(u)
    norma_v = np.linalg.norm(v)
    
    # Calcular a norma-2 da matriz A
    norma_A = np.linalg.norm(A, ord=2)
    
    return posto_A, norma_u * norma_v, norma_A

# Realizar o experimento para n = 5, 15, 25
valores_n = [5, 15, 25]
resultados = {}

for n in valores_n:
    resultados[n] = realizar_experimento(n)

# Imprimir os resultados
for n in valores_n:
    posto_A, norma_uv, norma_A = resultados[n]
    print(f"Para n = {n}:")
    print(f"Posto de u v^T: {posto_A}")
    print(f"||u||_2 * ||v||_2: {norma_uv}")
    print(f"||u v^T||_2: {norma_A}")
    print()
