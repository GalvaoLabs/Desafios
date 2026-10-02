# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

idade = int(input("Digite sua idade: "))
classificacao = input("Digite a classificação indicativa do filme ('L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior de 16', 'Maior de 18'): ")

def pode_ver_filme(idade, classificacao):
    if classificacao == 'L':
        print("Pode assistir o filme")

    elif classificacao == 'Maior de 12' and idade >= 12:
        print("Pode assistir o filme")

    elif classificacao == 'Maior de 14' and idade >= 14:
        print("Pode assistir o filme")

    elif classificacao == 'Maior de 16' and idade >= 16:
        print("Pode assistir o filme")

    elif classificacao == 'Maior de 18' and idade >= 18:
        print("Pode assistir o filme")

    else:
        print("Não pode assistir ao filme")

resposta = pode_ver_filme(idade,classificacao)
print(resposta)