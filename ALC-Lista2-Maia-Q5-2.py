# -*- coding: utf-8 -*-
"""
@author: bryan
"""

# Importa a biblioteca numpy para suporte a operações matemáticas em arrays e matrizes multidimensionais.
import numpy as np

# Define a função para verificar se uma matriz é ortogonal pela definição.
def is_orthogonal_by_definition(matrix):
    # Calcula a matriz identidade com o mesmo número de linhas da matriz de entrada.
    identity = np.eye(matrix.shape[0])
    
    # Calcula o produto da matriz pela sua transposta.
    product = np.dot(matrix, matrix.T)
    
    # Verifica se o produto é aproximadamente igual à matriz identidade, retorna True se for, False caso contrário.
    return np.allclose(product, identity)

# Define a função para verificar se uma matriz é ortogonal verificando se suas colunas têm comprimento unitário e são ortogonais entre si.
def is_orthogonal_by_vectors(matrix):
    # Calcula o comprimento de cada coluna da matriz.
    column_lengths = np.linalg.norm(matrix, axis=0)
    
    # Verifica se todos os comprimentos das colunas são aproximadamente iguais a 1 (comprimento unitário).
    unit_length = np.allclose(column_lengths, 1.0)
    
    # Calcula os produtos internos de todas as combinações de colunas.
    dot_products = np.dot(matrix.T, matrix)
    
    # Verifica se todos os produtos internos são aproximadamente iguais a zero, indicando ortogonalidade entre as colunas.
    is_orthogonal = np.allclose(dot_products, np.eye(matrix.shape[1]))
    
    # Retorna True se as colunas tiverem comprimento unitário e forem ortogonais, False caso contrário.
    return unit_length and is_orthogonal

# Matrizes fornecidas no exercício
P1 = np.array([[-0.58835, 0.70206, 0.40119],
               [-0.78446, -0.37524, -0.49377],
               [-0.19612, -0.60523, 0.77152]])

P2 = np.array([[-0.47624, -0.4264, 0.30151],
               [0.087932, 0.86603, -0.40825],
               [-0.87491, -0.26112, 0.86164]])

# Verifica se cada matriz é ortogonal usando as duas funções de verificação
is_orthogonal_P1_def = is_orthogonal_by_definition(P1)
is_orthogonal_P1_vec = is_orthogonal_by_vectors(P1)

is_orthogonal_P2_def = is_orthogonal_by_definition(P2)
is_orthogonal_P2_vec = is_orthogonal_by_vectors(P2)

# Imprime os resultados das verificações para ambas as matrizes
print("A matriz P1 é ortogonal pela definição:", is_orthogonal_P1_def)
print("A matriz P1 é ortogonal pelos vetores:", is_orthogonal_P1_vec)

print("\nA matriz P2 é ortogonal pela definição:", is_orthogonal_P2_def)
print("A matriz P2 é ortogonal pelos vetores:", is_orthogonal_P2_vec)

# Verifica se pelo menos uma das matrizes é ortogonal
is_orthogonal = is_orthogonal_P1_def or is_orthogonal_P1_vec or is_orthogonal_P2_def or is_orthogonal_P2_vec

# Imprime o resultado final
if is_orthogonal:
    print("\nPelo menos uma das matrizes é ortogonal.")
else:
    print("\nNenhuma das matrizes é ortogonal.")
