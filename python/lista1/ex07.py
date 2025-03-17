# 7. Ler uma lista de 10 números reais e mostre-os na ordem inversa.

# Lê uma lista de 10 números reais e mostra-os na ordem inversa.
numeros = []  # Inicializa uma lista vazia para armazenar os números
for i in range(10):  # Repete o processo 10 vezes
    numeros.append(float(input("Digite um número real: ")))  # Lê um número real e adiciona à lista
numeros.reverse()  # Inverte a ordem da lista
print(numeros)  # Exibe a lista na ordem inversa