# Imprime a mensagem de início do programa
print("=============== PROGRAMA PARA CALCULAR MEDIA ===============\n")

# Solicita o nome do aluno
name = input("Digite o nome do aluno: ")

# Solicita as notas do aluno
nota1 = float(input("Digite a primeira nota: "))  # Converte a nota para float
nota2 = float(input("Digite a segunda nota: "))  # Converte a nota para float
nota3 = float(input("Digite a terceira nota:"))  # Converte a nota para float

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Imprime o nome do aluno e sua média
print("O aluno ->", name, "ficou com a media:", media, "\n")

# Imprime o nome do aluno e sua média com duas casas decimais
print(f"O aluno  -> {name} ficou com a {media:.2f} \n")

# Verifica a situação do aluno com base na média
if media >= 6:  # Se a média for maior ou igual a 6, o aluno está aprovado
    print("O aluno está APROVADO!")
elif media > 4:  # Se a média for maior que 4 e menor que 6, o aluno está de recuperação
    print("O aluno está de RECUPERAÇÃO!")
else:  # Se a média for menor ou igual a 4, o aluno está reprovado
    print("O aluno está REPROVADO!")

# Imprime a mensagem de fim do programa
print("=============== FIM PROGRAMA ===============\n")