# -*- coding: utf-8 -*-
"""
@author: bryan
"""

def substituicao_regressiva(matriz, vetor):
    n = len(matriz)
    x = [0] * n  # Inicializa uma lista para armazenar a solucao
    
    # Para cada linha da matriz, comecando da ultima e indo ate a primeira
    for i in range(n-1, -1, -1):
        # Verifica se o elemento na diagonal principal e zero
        if matriz[i][i] == 0:
            raise ValueError("Um elemento nulo foi encontrado na diagonal da matriz triangular superior.")
        
        # Calcula o valor da variavel correspondente usando substituicao regressiva
        x[i] = vetor[i] / matriz[i][i]
        
        # Atualiza os valores do vetor coluna para as linhas acima
        for j in range(i-1, -1, -1):
            vetor[j] -= matriz[j][i] * x[i]
    
    return x

# Funcao para ler a matriz triangular superior
def ler_matriz_triangular_superior(n):
    matriz = []
    print("Digite os elementos da matriz triangular superior:")
    for i in range(n):
        linha = []
        for j in range(n):
            # Preenche com zeros abaixo da diagonal principal
            if j < i:
                linha.append(0)
            else:
                elemento = float(input(f"Digite o elemento da posicao ({i+1},{j+1}): "))
                linha.append(elemento)
        matriz.append(linha)
    return matriz

# Funcao para ler o vetor coluna
def ler_vetor_coluna(n):
    vetor = []
    print("Digite os elementos do vetor coluna:")
    for i in range(n):
        elemento = float(input(f"Digite o elemento {i+1} do vetor coluna: "))
        vetor.append(elemento)
    return vetor

# Programa principal
try:
    n = int(input("Digite a ordem da matriz: "))
    matriz = ler_matriz_triangular_superior(n)
    vetor = ler_vetor_coluna(n)
    
    # Chama a funcao para realizar a substituicao regressiva e exibe a solucao
    resultado = substituicao_regressiva(matriz, vetor)
    print("Solucao:", resultado)
except ValueError as e:
    print("Erro:", e)

