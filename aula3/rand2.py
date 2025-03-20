import numpy as np  # Importando a biblioteca numpy para realizar operações numéricas

# Gerando um array de 6 números aleatórios entre 0 e 60
# O tamanho do array é definido como (5,6), resultando em 5 linhas e 6 colunas
x = np.random.randint(0, 61, size=(5,6))  # Utilizando a função randint para gerar números aleatórios

# Imprimindo o array gerado para visualização
print(x)  # Exibindo o resultado no console