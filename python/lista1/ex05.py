# 5. Faça um programa que inicialize uma lista com vários números diferentes, depois disso, solicite ao usuário um número, verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado.


# Inicializa uma lista com vários números diferentes
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solicita ao usuário um número
numero_usuario = int(input("Digite um número: "))

# Verifica se o número está ou não na lista
if numero_usuario in lista_numeros:
    # Exibe uma mensagem notificando o usuário que o número está na lista
    print("O número está na lista.")
else:
    # Exibe uma mensagem notificando o usuário que o número não está na lista
    print("O número não está na lista.")