#Criar uma função para retornar se um número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))
print(par_impar(numero))

#def par_ou_impar(n):
#    return "Par" if n % 2 == 0 else "Ímpar"