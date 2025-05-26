#Crie a classe Funcionario com: Atributos: nome, salario. Método: exibir_dados(). Crie a classe Gerente que herda de Funcionario e adiciona: Atributo: departamento, Método sobrescrito: exibir_dados() mostrando também o departamento.

# Definição da classe Funcionario
class Funcionario:
    # Método construtor que inicializa os atributos nome e salario
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    # Método para exibir os dados do funcionário
    def exibir_dados(self):
        print(f'Nome: {self.nome}, Salário: {self.salario}')
        
# Definição da classe Gerente que herda de Funcionario
class Gerente(Funcionario):
    # Método construtor que inicializa os atributos nome, salario e departamento
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)  # Chama o construtor da classe pai
        self.departamento = departamento

    # Método sobrescrito para exibir os dados do gerente
    def exibir_dados(self):
        super().exibir_dados()  # Chama o método da classe pai
        print(f'Departamento: {self.departamento}')
        
# Criação de uma instância da classe Funcionario
funcionario = Funcionario("Carlos", 3000)

# Exibição dos dados do funcionário
funcionario.exibir_dados()

# Criação de uma instância da classe Gerente
gerente = Gerente("Ana", 5000, "Vendas")

# Exibição dos dados do gerente
gerente.exibir_dados()

