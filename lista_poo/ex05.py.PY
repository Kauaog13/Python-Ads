#Crie a classe Aluno com: Atributos: nome, nota1, nota2. Método: media() → retorna a média das duas notas, aprovado() → retorna True se média >= 7.

# Definição da classe Aluno
class Aluno:
    # Método construtor que inicializa os atributos nome, nota1 e nota2
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    # Método para calcular a média das notas
    def media(self):
        return (self.nota1 + self.nota2) / 2

    # Método para verificar se o aluno está aprovado
    def aprovado(self):
        return self.media() >= 7
    
# Criação de duas instâncias da classe Aluno
aluno1 = Aluno("Maria", 8, 6)
aluno2 = Aluno("João", 5, 6)

# Impressão da média do aluno
print(f'A média do aluno {aluno1.nome} é {aluno1.media()}')

# Impressão se o aluno está aprovado
print(f'O aluno {aluno1.nome} está aprovado? {"Sim" if aluno1.aprovado() else "Não"}')

# Impressão da média do aluno
print(f'A média do aluno {aluno2.nome} é {aluno2.media()}')

# Impressão se o aluno está aprovado
print(f'O aluno {aluno2.nome} está aprovado? {"Sim" if aluno2.aprovado() else "Não"}')