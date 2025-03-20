# 6. Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes diferentes digitados pelo usuário, depois disso solicite um número de 0 até 4 e remova o elemento desta posição.


nomes = []  # Inicializa uma lista vazia para armazenar os nomes
for i in range(5):  # Repete o processo 5 vezes para preencher a lista
    nome = input("Digite um nome: ")  # Solicita um nome do usuário
    nomes.append(nome)  # Adiciona o nome à lista
print(nomes)  # Exibe a lista preenchida

# Solicita um número de 0 até 4 para remover um elemento da lista
posicao = int(input("Digite um número de 0 até 4: "))

# Verifica se a posição é válida
if 0 <= posicao <= 4:
    del nomes[posicao]  # Remove o elemento da posição especificada
    print(nomes)  # Exibe a lista atualizada
else:
    print("Posição inválida")  # Exibe mensagem de erro se a posição for inválida