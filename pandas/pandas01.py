import pandas as pd #Importa a biblioteca Pandas

#Cria uma base de dados com linhas e colunas
dados = {
    'Nome':['João Pedro', 'Maria Cecilia', 'Antonio Marques', 'Ana Paula'],
    'Idade':[19,29,34,47],
    'Cidade':['Brasilia','Brasilia','Goiania','São Paulo'],
    'Area':['Tecnologia','Juridico','Gestão','TI']
}

#Imprime todos os dados
dt = pd.DataFrame(dados)
print("DataFrame Criado com os Dados:\n",dt)

#Imprime so as cidades
dt1 = dt['Cidade']
print("\nCidades: \n", dt1)

#Imprime so a cidade brasilia
dt2 = dt[dt['Cidade'] == 'Brasilia']
print("\n Apenas Brasilia: \n", dt2)