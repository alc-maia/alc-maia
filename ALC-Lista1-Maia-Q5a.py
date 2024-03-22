# -*- coding: utf-8 -*-
"""
@author: bryan
"""

import math

# Funcao para calcular a posicao do efetuador final
def calcular_posicao_efetuador(theta1, theta2, L1, L2):
    # Calcula as coordenadas X e Y do efetuador final
    X_U = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
    Y_U = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)
    
    return round(X_U, 1), round(Y_U, 1)

# Programa principal
try:
    # Entrada dos angulos theta1 e theta2 em graus
    theta1 = math.radians(float(input("Digite o angulo theta1 em graus: ")))
    theta2 = math.radians(float(input("Digite o angulo theta2 em graus: ")))
    
    # Comprimentos dos elos
    L1 = 20.0
    L2 = 15.0
    
    # Calcula e imprime a posicao do efetuador final
    X_U, Y_U = calcular_posicao_efetuador(theta1, theta2, L1, L2)
    print("Posicao do efetuador final (X_U, Y_U):", X_U, Y_U)
except ValueError:
    print("Erro: Digite um valor numerico valido para os angulos theta1 e theta2.")
