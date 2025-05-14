class Msg(): # cria uma classe chamada Msg
    def exibir_msg(self): # cria um método para exibir uma mensagem
        print("Hello World") # imprime a mensagem "Hello World"

# Exemplo de uso da classe Msg
instancia = Msg() # cria uma instância da classe Msg
instancia.exibir_msg() # chama o método exibir_msg da instância

class Carro: # cria uma classe chamada Carro
    def __init__(self, marca, modelo, ano, cor): # método construtor com os atributos marca, modelo, ano e cor
        self.marca = marca #self.marca = objt / marca = atributo
        self.modelo = modelo # atribui o valor de modelo ao atributo da instância
        self.ano = ano 
        self.cor = cor 
    
carro = Carro("BMW", "X6", 2024, "Azul") # cria uma instância da classe Carro com valores específicos

print(f'O carro é {carro.marca}') # imprime a marca do carro
print(f'O modelo é {carro.modelo}') 
print(f'O ano é {carro.ano}') 
print(f'A cor é {carro.cor}') 
