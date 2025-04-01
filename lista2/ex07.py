#Criar uma função para gerar uma matriz 10x10 (array) de forma aleatória.

import random

def gerar_matriz_aleatoria(tamanho=10):
    matriz = [[random.randint(0, 100) for _ in range(tamanho)] for _ in range(tamanho)]
    print("Matriz Aleatória:")
    for linha in matriz:
        print(linha)
    return matriz

gerar_matriz_aleatoria()
