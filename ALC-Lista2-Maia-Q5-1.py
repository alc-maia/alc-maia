# -*- coding: utf-8 -*-
"""
@author: bryan
"""
# Importa a biblioteca numpy, que fornece suporte para operacoes matematicas em arrays e matrizes multidimensionais.
import numpy as np  

def is_orthogonal_by_definition(matrix, atol=1e-4, rtol=1e-4):
    # Cria uma matriz identidade com o mesmo número de linhas da matriz de entrada.
    identity = np.eye(matrix.shape[0])
    # Calcula o produto da matriz pela sua transposta.
    product = np.dot(matrix, matrix.T)
    # Compara o produto com a matriz identidade usando tolerâncias especificadas e retorna True se forem próximas.
    return np.allclose(product, identity, atol=atol, rtol=rtol)

def is_orthogonal_by_vectors(matrix, atol=1e-4, rtol=1e-4):
    # Calcula a norma (comprimento) de cada coluna da matriz.
    column_lengths = np.linalg.norm(matrix, axis=0)
    # Verifica se todas as colunas têm comprimento unitário dentro das tolerâncias especificadas.
    unit_length = np.allclose(column_lengths, 1.0, atol=atol, rtol=rtol)
    # Calcula os produtos internos entre todas as colunas da matriz.
    dot_products = np.dot(matrix.T, matrix)
    # Verifica se todos os produtos internos são próximos de zero para colunas diferentes e 1 para a mesma coluna.
    is_orthogonal = np.allclose(dot_products, np.eye(matrix.shape[1]), atol=atol, rtol=rtol)
    # Retorna True se as colunas tiverem comprimento unitário e forem mutuamente ortogonais.
    return unit_length and is_orthogonal

# Matrizes fornecidas no exercício
P1 = np.array([[-0.40825, 0.43644, 0.80178],
               [-0.8165, 0.21822, -0.53452],
               [-0.40825, -0.87287, 0.26726]])

P2 = np.array([[-0.51450, 0.48507, 0.70711],
               [-0.68599, -0.72761, 0.0],
               [0.51450, -0.48507, 0.70711]])

# Testa a matriz P1 usando ambas as funções de verificação de ortogonalidade e imprime os resultados.
print("Matrix P1 is orthogonal by definition:", is_orthogonal_by_definition(P1))
print("Matrix P1 is orthogonal by vectors:", is_orthogonal_by_vectors(P1))

# Testa a matriz P2 usando ambas as funções de verificação de ortogonalidade e imprime os resultados.
print("\nMatrix P2 is orthogonal by definition:", is_orthogonal_by_definition(P2))
print("Matrix P2 is orthogonal by vectors:", is_orthogonal_by_vectors(P2))
