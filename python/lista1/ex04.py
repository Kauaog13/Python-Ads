# 4. Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes de cidades, um por vez, cada vez que o usuário digitar um nome, o programa deve incluir este nome na lista de cidades.


cidades = [input("Digite o nome de uma cidade: ") for _ in range(3)]  # Solicita 3 nomes de cidades ao usuário e armazena em uma lista
print("Lista de cidades:", cidades)  # Exibe a lista de cidades