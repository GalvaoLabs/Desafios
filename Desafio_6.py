# Crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseado no periodo do dia
# Periodos :    Manhã: 5 até 12, Tarde: 13 até 18, Noite: 18 até 24

# Exemplo: 
# Nome: Allana
# Hora : 9
# Bom dia, Allana

# Exemplo2: 
# Nome: Gustavo B
# Hora : 15
# Boa Tarde, Gustavo B

nome = input("Digite seu nome: ")
hora = int(input("Digite um número inteiro de 5 a 24, correspondente a hora do dia: "))

def cumprimentar(nome, hora):
    if 5 <= hora <= 12:
        print(f"Nome: {nome}")
        print(f"\nHora: {hora}")
        print(f"Bom dia, {nome}")

    elif 13 <= hora <18:
        print(f"Nome: {nome}")
        print(f"Hora: {hora}")
        print(f"Boa Tarde, {nome}")

    elif 18 <= hora <=24:
        print(f"Nome: {nome}")
        print(f"\nHora: {hora}")
        print(f"Boa Noite, {nome}")

    else: 
        print("O Valor digitado não corresponde a um número inteiro de 5 a 24!")

cumprimentar(nome,hora)