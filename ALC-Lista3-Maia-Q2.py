def crossprod(u, v):
    # Calcula o produto vetorial de dois vetores u e v
    cross_product = [
        u[1] * v[2] - u[2] * v[1],  # Componente x do produto vetorial
        u[2] * v[0] - u[0] * v[2],  # Componente y do produto vetorial
        u[0] * v[1] - u[1] * v[0]   # Componente z do produto vetorial
    ]
    return cross_product  # Retorna o vetor resultante do produto vetorial

def dotprod(u, v):
    # Calcula o produto escalar de dois vetores u e v
    dot_product = sum(u[i] * v[i] for i in range(len(u)))
    return dot_product  # Retorna o produto escalar

u = [1, 2, 3]
v = [4, 5, 6]

# Calcula u × v
u_cross_v = crossprod(u, v)
print("u × v =", u_cross_v)  # Saida esperada: [-3, 6, -3]

# Calcula v × u
v_cross_u = crossprod(v, u)
print("v × u =", v_cross_u)  # Saida esperada: [3, -6, 3]

# Calcula ⟨u × v, u⟩
dot_u_cross_v_u = dotprod(u_cross_v, u)
print("⟨u × v, u⟩ =", dot_u_cross_v_u)  # Saida esperada: 0

# Calcula ⟨v × u, v⟩
dot_v_cross_u_v = dotprod(v_cross_u, v)
print("⟨v × u, v⟩ =", dot_v_cross_u_v)  # Saida esperada: 0
