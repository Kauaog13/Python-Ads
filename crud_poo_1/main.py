from cliente_DAO import ClienteDAO
from cliente import Cliente
from datetime import datetime

#Criando um Cliente
dao = ClienteDAO()
cliente1 = Cliente(idCliente= None, nome='Maria Alves', tel='9999-9999', email='mariaa@gmail.com', cidade='default', data_cadastro=datetime.now())
dao.criar(cliente1)

#listar os clientes
clientes = dao.listar()
print("Listando os Clientes")
for c in clientes:
    print(c)
    
#Atualizando os dados
cliente1 = clientes[1]
cliente1.nome = 'Maria Souza'
cliente1.tel = '9999-9999'
cliente1.email = 'marias@gmail.com'
cliente1.cidade = 'Goiania'
cliente1.data_cadastro = datetime.now()
dao.atualizar(cliente1)

#Listar os dados atualizando
clientes = dao.listar()
print("\n Após atualização: ")
for c in dao.listar():
    print(c)