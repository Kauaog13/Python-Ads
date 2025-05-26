#Crie a classe Carro com: Atributos: modelo, velocidade. Métodos: acelerar(valor) → aumenta a velocidade, frear(valor) → diminui a velocidade (mínimo 0), mostrar_velocidade().

# Definição da classe Carro
class Carro:
    def __init__(self, modelo, velocidade=0):  # Método construtor que inicializa os atributos modelo e velocidade
        self.modelo = modelo
        self.velocidade = velocidade

    # Método para aumentar a velocidade do carro
    def acelerar(self, valor):
        self.velocidade += valor
        print(f'O carro {self.modelo} acelerou para {self.velocidade} km/h')

    # Método para diminuir a velocidade do carro
    def frear(self, valor):
        if self.velocidade - valor < 0:
            self.velocidade = 0
        else:
            self.velocidade -= valor
        print(f'O carro {self.modelo} reduziu a velocidade para {self.velocidade} km/h')

    # Método para mostrar a velocidade atual do carro
    def mostrar_velocidade(self):
        print(f'A velocidade atual do carro {self.modelo} é {self.velocidade} km/h')
        
# Criação de uma instância da classe Carro
carro1 = Carro("Fusca")

# Acelerando o carro
carro1.acelerar(50)

# Mostrando a velocidade atual do carro
carro1.mostrar_velocidade()

# Freando o carro
carro1.frear(20)