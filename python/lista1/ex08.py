# 8. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

# Lê uma lista de 5 números inteiros
numeros = []  # Inicializa uma lista vazia para armazenar os números
for i in range(5):  # Repete o processo 5 vezes
    numeros.append(int(input("Digite um número: ")))  # Lê um número e adiciona à lista
# Mostra cada número juntamente com a sua posição na lista
for i, num in enumerate(numeros):  # Percorre a lista com índice e valor
    print(f"Número {num} está na posição {i}")  # Exibe o número e sua posição