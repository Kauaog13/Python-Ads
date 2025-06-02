class Cliente:
    def __init__(self, idCliente=None, nome=None, tel=None, email=None, cidade=None, data_cadastro=None):
        self.idCliente = idCliente
        self.nome = nome
        self.tel = tel
        self.email = email
        self.cidade = cidade
        self.data_cadastro = data_cadastro
    def __str__(self):
        return f"id: {self.idCliente} | Nome: {self.nome} | Telefone: {self.tel} | Email: {self.email} | Cidade: {self.cidade} | Data: {self.data_cadastro}"