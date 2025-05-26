#Crie uma classe Retangulo com: Atributos: largura e altura. Métodos: calcular_area(), calcular_perimetro(). Crie um objeto, atribua valores e mostre área e perímetro.

# Definição da classe Retangulo
class Retangulo:
    def __init__(self, largura, altura): # Método construtor que inicializa os atributos largura e altura
        self.largura = largura
        self.altura = altura
        
    # Método para calcular a área do retângulo
    def calcular_area(self): 
        return self.largura * self.altura
    
    # Método para calcular o perímetro do retângulo
    def calcular_perimetro(self): 
        return 2 * (self.largura + self.altura)
    
# Criação de uma instância da classe Retangulo
retangulo = Retangulo(5, 10)

# Impressão da área e perímetro do retângulo criado
print(f'A área do retângulo é {retangulo.calcular_area()} unidades quadradas')

# Impressão do perímetro do retângulo criado
print(f'O perímetro do retângulo é {retangulo.calcular_perimetro()} unidades')
    