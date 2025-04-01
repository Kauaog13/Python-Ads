#Faça um programa que tenha uma lista pronta chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números da lista e colocá-los em outra lista.
# A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
# (Utilize o import random e a função sorteados ficará parcialmente: sorteados = random.sample(lista, 5)).

import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def sorteia():
    sorteados = random.sample(numeros, 5)
    return sorteados

def somaPar():
    sorteados = sorteia()
    soma = sum(num for num in sorteados if num % 2 == 0)
    print(f'Os números sorteados foram: {sorteados}')
    print(f'A soma dos números pares é: {soma}')

somaPar()