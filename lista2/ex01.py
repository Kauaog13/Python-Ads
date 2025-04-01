#Crie uma função para calcular as quatro operações da matemática (soma, subtração, divisão e multiplicação) sendo fornecidos 2 números e informando o resultado de cada operação.

import random

def calculadora(a, b):
    print(f'Soma: {a + b}')
    print(f'Subtração: {a - b}')
    print(f'Multiplicação: {a * b}')
    print(f'Divisão: {a / b if b != 0 else "Divisão por zero não é permitida"}')

calculadora(10,20)