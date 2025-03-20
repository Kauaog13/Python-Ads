# Solicita ao usuário que digite um número para verificar se é par ou ímpar
num = int(input("Digite um número para saber se é PAR OU ÍMPAR: "))

# Verifica se o número é ímpar (resto da divisão por 2 é diferente de 0)
if num % 2:
    # Exibe a mensagem caso o número seja ímpar
    print("Esse número é ÍMPAR!")
else:
    # Exibe a mensagem caso o número seja par
    print("Esse número é PAR!")