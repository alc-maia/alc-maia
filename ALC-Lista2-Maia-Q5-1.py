# -*- coding: utf-8 -*-
"""
@author: bryan
"""

# Importa a biblioteca numpy, que fornece suporte para operacoes matematicas em arrays e matrizes multidimensionais.
import numpy as np

# Define a funcao is_orthogonal_by_definition para verificar se uma matriz e ortogonal pela definicao.
def is_orthogonal_by_definition(matrix):
    # Verifica se a matriz satisfaz a definicao de ortogonalidade.
    
    # Cria uma matriz identidade com o mesmo numero de linhas que a matriz de entrada.
    identity = np.eye(matrix.shape[0])
    
    product = np.dot(matrix, matrix.T)
    
    # Compara o produto com a matriz identidade e retorna True se forem aproximadamente iguais, caso contrario retorna False.
    return np.allclose(product, identity)

# Define a funcao is_orthogonal_by_vectors para verificar se uma matriz e ortogonal verificando se suas colunas tem comprimento unitario e sao ortogonais entre si.
def is_orthogonal_by_vectors(matrix):
    # Verifica se as colunas da matriz tem comprimento unitario e sao ortogonais.
    
    # Calcula o comprimento de cada coluna da matriz.
    column_lengths = np.linalg.norm(matrix, axis=0)
    
    # Verifica se todos os comprimentos das colunas sao aproximadamente iguais a 1 (comprimento unitario).
    unit_length = np.allclose(column_lengths, 1.0)
    
    # Calcula os produtos internos de todas as combinacoes de colunas.
    dot_products = np.dot(matrix.T, matrix)
    
    # Verifica se todos os produtos internos sao aproximadamente iguais a zero, indicando ortogonalidade entre as colunas.
    is_orthogonal = np.allclose(dot_products, np.eye(matrix.shape[1]))
    
    # Retorna True se as colunas tiverem comprimento unitario e forem ortogonais, caso contrario retorna False.
    return unit_length and is_orthogonal

# Define as matrizes de teste P1 e P2 fornecidas no exercicio.
P1 = np.array([[-0.40825, 0.43644, 0.80178],
               [-0.8165, 0.21822, -0.53452],
               [-0.40825, -0.87287, 0.26726]])

P2 = np.array([[-0.51450, 0.48507, 0.70711],
               [-0.68599, -0.72761, 0.0],
               [0.51450, -0.48507, 0.70711]])

# Testa as matrizes usando ambas as funcoes de verificacao de ortogonalidade.
print("Matrix P1 is orthogonal by definition:", is_orthogonal_by_definition(P1))
print("Matrix P1 is orthogonal by vectors:", is_orthogonal_by_vectors(P1))

print("\nMatrix P2 is orthogonal by definition:", is_orthogonal_by_definition(P2))
print("Matrix P2 is orthogonal by vectors:", is_orthogonal_by_vectors(P2))
