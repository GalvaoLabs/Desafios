# Um professor quer sortear um dos seus quatro alunos para ajudar o Rian.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
### importando a biblioteca random
from random import choice
nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]

escolhido = choice(nomes)

print(f"O {escolhido} foi escolhido para ajudar o Rian")