#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    área_terreno = largura * comprimento
    print(f'A área do terreno é de {área_terreno} metros quadrados.')

largura_terreno = float(input('Digite a largura do terreno: '))
comprimento_terreno = float(input('Digite o comprimento do terreno: '))
área(largura_terreno, comprimento_terreno)