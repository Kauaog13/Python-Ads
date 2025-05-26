# Crie a classe Produto com: Atributos: nome, preco, quantidade. Métodos: vender(qtd), repor(qtd), exibir_estoque().

# Definição da classe Produto
class Produto:
    # Método construtor que inicializa os atributos nome, preco e quantidade
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Método para vender uma quantidade do produto
    def vender(self, qtd):
        if qtd > self.quantidade:
            print(f'Não há estoque suficiente para vender {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}.')
        else:
            self.quantidade -= qtd
            print(f'Vendido {qtd} unidades de {self.nome}. Estoque restante: {self.quantidade}.')

    # Método para repor uma quantidade do produto
    def repor(self, qtd):
        self.quantidade += qtd
        print(f'Reposto {qtd} unidades de {self.nome}. Estoque atual: {self.quantidade}.')

    # Método para exibir o estoque do produto
    def exibir_estoque(self):
        print(f'Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade em estoque: {self.quantidade}')
        
# Criação de uma instância da classe Produto
produto1 = Produto("Camiseta", 29.90, 100)

# Exibição do estoque do produto
produto1.exibir_estoque()

# Venda de 20 unidades do produto
produto1.vender(20)

# Reposição de 50 unidades do produto
produto1.repor(50)

