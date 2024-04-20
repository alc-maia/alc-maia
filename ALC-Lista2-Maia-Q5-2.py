# -*- coding: utf-8 -*-
"""
@author: bryan
"""
# Importa a biblioteca numpy para suporte a operações matemáticas em arrays e matrizes multidimensionais.
import numpy as np 

def is_orthogonal_by_definition(matrix, atol=1e-4, rtol=1e-4):
    """ Verifica ortogonalidade de uma matriz pela definição. """
    identity = np.eye(matrix.shape[0])
    product = np.dot(matrix, matrix.T)
    return np.allclose(product, identity, atol=atol, rtol=rtol)

def is_orthogonal_by_vectors(matrix, atol=1e-4, rtol=1e-4):
    """ Verifica ortogonalidade de uma matriz pelas propriedades vetoriais das colunas. """
    column_lengths = np.linalg.norm(matrix, axis=0)
    unit_length = np.allclose(column_lengths, 1.0, atol=atol, rtol=rtol)
    dot_products = np.dot(matrix.T, matrix)
    is_orthogonal = np.allclose(dot_products, np.eye(matrix.shape[1]), atol=atol, rtol=rtol)
    return unit_length and is_orthogonal

# Matrizes fornecidas
P1 = np.array([
    [-0.58835, 0.70206, 0.40119],
    [-0.78446, -0.37524, -0.49377],
    [-0.19612, -0.60523, 0.77152]
])

P2 = np.array([
    [-0.47624, -0.4264, 0.30151],
    [0.087932, 0.86603, -0.40825],
    [-0.87491, -0.26112, 0.86164]
])

# Testa as matrizes usando ambas as funções de verificação de ortogonalidade.
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
print("\nPelo menos uma das matrizes é ortogonal." if is_orthogonal else "\nNenhuma das matrizes é ortogonal.")
