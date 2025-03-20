import numpy as np

# Geração de uma matriz 4x4 com valores aleatórios entre 10 e 100
x = np.random.randint(10, 100, size = (4,4))

# Cálculo do maior valor da matriz
maior_valor = x.max()

# Cálculo do menor valor da matriz
menor_valor = x.min()

# Cálculo da soma dos valores da matriz
soma_valores = x.sum()

# Impressão da matriz gerada
print("Matriz:")
print(x)

# Impressão dos resultados
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Soma dos valores: {soma_valores}")