#Crie a classe ContaBancaria com: Atributos privados: __titular, __saldo. Métodos: depositar(valor), sacar(valor), exibir_saldo(). Garanta que não seja possível sacar mais que o saldo.

# Definição da classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo=0):  # Método construtor que inicializa os atributos privados __titular e __saldo
        self.__titular = titular
        self.__saldo = saldo

    # Método para depositar um valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de {valor} realizado com sucesso! Novo saldo: R${self.__saldo},00')
        else:
            print('Valor de depósito inválido!')

    # Método para sacar um valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de {valor} realizado com sucesso! Novo saldo: R${self.__saldo},00')
        else:
            print('Saque inválido! Verifique o valor e o saldo disponível.')

    # Método para exibir o saldo atual da conta
    def exibir_saldo(self):
        print(f'Saldo atual da conta de {self.__titular}: R${self.__saldo},00')
        
# Criação de uma instância da classe ContaBancaria
conta1 = ContaBancaria("João", 1000)

# Exibindo o saldo inicial
conta1.exibir_saldo()

# Depositando um valor
conta1.depositar(500)

# Sacando um valor
conta1.sacar(200)

# Tentando sacar um valor maior que o saldo
conta1.sacar(2000)

# Tentando depositar um valor inválido
conta1.depositar(-100)
