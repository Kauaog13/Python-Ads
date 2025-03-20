import numpy as np

# Gera uma lista de 10 números aleatórios entre 1 e 100
lista = np.random.randint(1,100,size=10)  # Cria uma lista de números aleatórios
print(lista)  # Exibe a lista gerada

# Inicializa uma variável para contar os números pares
pares = 0  # Inicializa a contagem de números pares

# Percorre a lista para contar os números pares
for i in lista:  # Itera sobre cada elemento da lista
    # Verifica se o número é par
    if i % 2 == 0:  # Verifica se o número é divisível por 2
        # Incrementa a contagem de números pares
        pares += 1  # Incrementa a contagem de números pares
        # Outro jeito: pares = pares + 1

# Exibe a quantidade de números pares encontrados
print(f"Existem {pares} números pares na lista")  # Exibe o resultado