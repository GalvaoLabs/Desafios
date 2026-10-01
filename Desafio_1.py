# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
PORCENTAGEM = 15
salario = float(input(f"Digite o salário do funcionário que receberá {PORCENTAGEM}% de aumento: "))
aumento = (salario * PORCENTAGEM) / 100
cal_salario = salario + aumento

print(f"O Seu salário atual é de R${salario} com o aumento de {PORCENTAGEM}% seu novo salário será de R${cal_salario}")