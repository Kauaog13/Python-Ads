class Usuario:
    def __init__(self, id=None, nome=None, email=None):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email}"
