# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

idade = int(input("Digite sua idade: "))
classificacao = input("Digite a classificação indicativa do filme ('L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'): ")

def pode_ver_filme(idade, classificacao):
    if 