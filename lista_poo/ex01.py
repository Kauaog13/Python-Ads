#Crie uma classe chamada Pessoa com os atributos: nome, idade. Inclua um método apresentar que imprime: "Olá, meu nome é <nome> e tenho <idade> anos."

# Definição da classe Pessoa
class Pessoa:
    # Método construtor que inicializa os atributos nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade            

# Criação de uma instância da classe Pessoa
pessoa1 = Pessoa("Kauã", 21)

# Impressão das informações da pessoa criada
print(f'O nome da pessoa é {pessoa1.nome} e a idade é {pessoa1.idade} anos') 