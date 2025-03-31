def msg():
    print("-"*30)
    print("       Funções em Python")
    print("-"*30)
msg()



#def soma1(a, b):
    #sum = a + b
    #print(f"A soma dos valores é: {sum}")
#soma1(5,6)



def calc(x, y):
    # Calcula a soma
    soma = x + y
    # Calcula a subtração
    sub = x - y
    # Calcula a multiplicação
    mult = x * y
    # Calcula a divisão
    div = x / y

    # Retorna os resultados das operações
    return soma, sub, mult, div

# Solicita os valores do usuário
v1 = float(input("Digite o primeiro valor:"))
v2 = float(input("Digite o segundo valor:"))

# Chama a função calc e armazena os resultados
soma, sub, mult, div = calc(v1,v2)

# Imprime os resultados
print(f"\nA soma dos valores é: {soma}")
print(f"A subtração dos valores é: {sub}")
print(f"A multiplicação dos valores é: {mult}")
print(f"A divisão dos valores é: {div}")

msg()