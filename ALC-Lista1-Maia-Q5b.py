# -*- coding: utf-8 -*-
"""
@author: bryan
"""

import math
import numpy as np

# Funcao para calcular a matriz de rotacao em 2D
def matriz_rotacao(theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])

# Funcao para calcular a matriz de transformacao homogenea
def calcular_matriz_transformacao(theta1, theta2, L1, L2):
    # Matrizes de rotacao para theta1 e theta2
    R1 = matriz_rotacao(theta1)
    R2 = matriz_rotacao(theta2)

    # Translacoes para os comprimentos dos elos
    T1 = np.array([[1, 0, L1], [0, 1, 0], [0, 0, 1]])
    T2 = np.array([[1, 0, L2], [0, 1, 0], [0, 0, 1]])

    # Calcula a matriz de transformacao total
    T = np.dot(np.dot(R1, T1), np.dot(R2, T2))
    
    return T

# Programa principal
try:
    # Entrada dos angulos theta1 e theta2 em graus
    theta1 = math.radians(float(input("Digite o angulo theta1 em graus: ")))
    theta2 = math.radians(float(input("Digite o angulo theta2 em graus: ")))
    
    # Comprimentos dos elos
    L1 = 20.0
    L2 = 15.0
    
    # Calcula a matriz de transformacao
    T = calcular_matriz_transformacao(theta1, theta2, L1, L2)
    print("Matriz de Transformacao T:")
    print(T)
except ValueError:
    print("Erro: Digite um valor numerico valido para os angulos theta1 e theta2.")
