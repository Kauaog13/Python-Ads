#Faça uma função chamada somalimposto. A função possui dois parâmetros: 
# taxaimposto, que é a porcentagem de imposto sobre vendas. custo, que é o custo de um item antes do imposto. 
# A função retorna o valor do custo alterado para incluir o imposto sobre vendas.

def somalimposto(taxaimposto, custo):
    return custo + (custo * taxaimposto / 100)

print(somalimposto(10, 100))