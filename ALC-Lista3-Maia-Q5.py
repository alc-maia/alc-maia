import numpy as np
import matplotlib.pyplot as plt

def wilkinson_bidiagonal_matrix(n):
    # Inicializa uma matriz de zeros de dimensão n x n
    A = np.zeros((n, n))
    
    # Preenche a matriz bidiagonal de Wilkinson
    for i in range(n):
        A[i, i] = n - i
        if i < n - 1:
            A[i, i + 1] = n

    return A

# Item (b) - Plotar o número de condição das matrizes bidiagonais de Wilkinson de ordens 1 a 15
orders = range(1, 16) # Ordem das matrizes bidiagonais de Wilkinson
condition_numbers = [] # Lista para armazenar os números de condição

for n in orders:
    A = wilkinson_bidiagonal_matrix(n) # Matriz bidiagonal de Wilkinson de ordem n
    cond_number = np.linalg.cond(A) # Número de condição da matriz A
    condition_numbers.append(cond_number) # Adiciona o número de condição à lista

plt.figure(figsize=(10, 6))
plt.plot(orders, condition_numbers, marker='o')
plt.xlabel('Ordem da Matriz (n)')
plt.ylabel('Número de Condição')
plt.title('Número de Condição das Matrizes Bidiagonais de Wilkinson de Ordem 1 a 15')
plt.grid(True)
plt.show()

# Parte (c) - Analisar os autovalores da matriz 20x20 de Wilkinson e a matriz perturbada
n = 20
A = wilkinson_bidiagonal_matrix(n)
#print(A)

# Calcular os autovalores de A
eigenvalues_A = np.linalg.eigvals(A)

# Perturbar o elemento A(20,1) da matriz em por 10^-10
A_perturbed = A.copy()
A_perturbed[19, 0] += 1e-10 # A[19,0] representa o elemento A(20,1) da matriz

# Calcular os autovalores da matriz perturbada
eigenvalues_A_perturbed = np.linalg.eigvals(A_perturbed)

# Comparar os autovalores
print("Autovalores de A:")
print(eigenvalues_A)
print("\nAutovalores de A perturbada:")
print(eigenvalues_A_perturbed)

# Calcular a magnitude da perturbação nos autovalores
perturbation_magnitude = np.abs(eigenvalues_A - eigenvalues_A_perturbed)
print("\nMagnitude da perturbação nos autovalores:")
print(perturbation_magnitude)