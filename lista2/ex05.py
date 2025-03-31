#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado pelo usuário.



def quantidade_digitos():
    numero = int(input("Digite um número inteiro: "))
    quantidade = len(str(abs(numero)))
    print(f"A quantidade de dígitos do número {numero} é {quantidade}.")

quantidade_digitos()