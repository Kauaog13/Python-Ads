# 2. Escreva um programa que leia e mostre uma lista de 10 elementos inteiros. Em seguida, conte quantos valores pares existem na lista, por fim, exiba a quantidade na tela.


lista  = [int(input("Digite o {i+1}° número: ")) for i in range(10)]  # Lê 10 números inteiros do usuário e armazena em uma lista
pares = [n for n in lista if n % 2 == 0]  # Filtra os números pares da lista

print("Lista:", lista)  # Exibe a lista de números inteiros
print("Quantidade de pares:", len(pares))  # Exibe a quantidade de números pares