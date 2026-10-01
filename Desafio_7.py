# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00

valor_conta = float(input("Digite o valor da conta: "))
qualidade_servico = input("Digite a qualidade do serviço ('ruim', 'medio', 'bom', 'excelente'): ")

def calculo_gorjeta(valor_conta, qualidade_servico):
    if qualidade_servico == 'excelente':
        cal_gorjeta = (valor_conta * 5) / 100
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {qualidade_servico}")
        print(f"O valor da gorjeta é de R$ {cal_gorjeta:.2f}")

    elif qualidade_servico == 'bom':
        cal_gorjeta = (valor_conta * 4) / 100
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {qualidade_servico}")
        print(f"O valor da gorjeta é de R$ {cal_gorjeta:.2f}")

    elif qualidade_servico == 'media':
        cal_gorjeta = (valor_conta * 2.5) / 100
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {qualidade_servico}")
        print(f"O valor da gorjeta é de R$ {cal_gorjeta:.2f}")

    elif qualidade_servico == 'ruim':
        cal_gorjeta = (valor_conta * 0) / 100
        print(f"O valor da conta é: {valor_conta}")
        print(f"A qualidade do serviço é: {qualidade_servico}")
        print(f"O valor da gorjeta é de R$ {cal_gorjeta:.2f}")

    else:
        print("A qualidade do serviço digitada não é válida!!!")

calculo_gorjeta(valor_conta, qualidade_servico)