#LISTAS SIMPLES []

# Cria uma lista com elementos de diferentes tipos (strings e números)
lista = ["Senac","Curso","Tecnologia","ADS",2025,3.25]  # Define uma lista com elementos de diferentes tipos
# Imprime a lista completa no console
print(lista)  # Exibe a lista completa no console
# Verifica e imprime o tipo de dado da variável lista
print(type(lista))  # Verifica e exibe o tipo de dado da variável lista
# Acessa e imprime o terceiro elemento da lista (índice 2)
print(lista[2])  # Acessa e exibe o terceiro elemento da lista (índice 2)
# Adiciona um novo elemento à lista
lista.append("Fim da aula")
# Exibe a lista atualizada
print(lista)
# Remove o elemento "ADS" da lista
lista.remove("ADS")
# Exibe a lista atualizada
print(lista)

#LISTA DO TIPO TUPLA()

# Cria uma tupla com elementos de diferentes tipos (strings e números)
tup = ("Senac","Curso","Tecnologia","ADS",True,2025,3.25)  # Define uma tupla com elementos de diferentes tipos
# Imprime a tupla completa no console
print(tup)  # Exibe a tupla completa no console
# Verifica e imprime o tipo de dado da variável tupla
print(type(tup))  # Verifica e exibe o tipo de dado da variável tupla
# Acessa e imprime o quinto elemento da tupla (índice 4)
print(tup[4])  # Acessa e exibe o quinto elemento da tupla (índice 4)

#LISTA DO TIPO DICIONARIO {}

# Cria um dicionário com chave-valor
dic = {"id":140, "nome":"Professor ling", "cpf":12345, "estudadante":True}  # Define um dicionário com chave-valor
# Imprime o dicionário completo no console
print(dic)  # Exibe o dicionário completo no console
# Verifica e imprime o tipo de dado da variável dicionário
print(type(dic))  # Verifica e exibe o tipo de dado da variável dicionário
# Acessa e imprime o valor da chave "id" no dicionário
print(dic["id"])  # Acessa e exibe o valor da chave "id" no dicionário

#LISTA DO TIPO CONJUNTO - Set

# Cria um conjunto com elementos de diferentes tipos (strings, números e booleanos)
conj = {"Aula",11, False, 3.4,11}  # Define um conjunto com elementos de diferentes tipos
# Imprime o conjunto no console
print(conj)  # Exibe o conjunto no console
# Verifica e imprime o tipo de dado da variável conjunto
print(type(conj))  # Verifica e exibe o tipo de dado da variável conjunto