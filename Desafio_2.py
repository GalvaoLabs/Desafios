# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9

numero = int(input("Digite um número inteiro para saber seu sucessor e antecessor: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"\n\nO número que você digitou é: {numero}")
print(f"\nO sucessor de {numero} é: {sucessor}")
print(f"O antecessor do {numero} é: {antecessor}")