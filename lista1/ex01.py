# 1. Escreva um programa que receba uma lista de 10 inteiros via teclado, em seguida o programa deve solicitar um número e informar se o número também está na lista ou não. 


# Recebe uma lista de 10 inteiros via teclado
lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

# Solicita um número para buscar na lista
num = int(input("Digite um número para buscar na lista: "))

# Verifica se o número está na lista e imprime a resposta
print("O número está na lista." 
      if num in lista 
      else "O número não está na lista.")
