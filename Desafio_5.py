# Agora vamos dar uma relembrada na aula de funções, pegue o código do exercicio anterior e transfome numa função,
# essa função deve receber uma lista e dessa lista escolher algum nome e dar um print
# ou seja vocês vão precisar criar a função e depois "chamar" a mesma para que ela execute.

from random import choice

nomes = ["Miguel", "Kaio", "Leonardo", "Gustavo A"]

def escolha(nomes):
    escolhido = choice(nomes)
    print(f"O {escolhido} foi escolhido para ajudar o Rian")

nomes2 = ['Anna', 'Beatriz', 'Enzo', 'Marcos']
escolha(nomes2)