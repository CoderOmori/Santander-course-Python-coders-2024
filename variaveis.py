# > Variáveis

# 1. Variáveis

idade = 24 #"idade recebe 24"

print(idade)

Legolas = 'gato'

print(Legolas)

"""
Tipos de variáveis

1. int: números inteiros
2. float: números reais
3. str: cadeias de caracteres/dados 
4. bool: valores lógicos: true ou false

type: tipo da variavel
"""
idade = 24
altura = 1.59
nome = "Jessica Omori"
estudando = True


print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))


#obtendo dados do usuário e salvando em variáveis

linguagem = input('qual é a linguagem de programação que você está estudando?')
idade = input('Qual a sua idade?')

print("A linguagem que você está estudando é", linguagem)
print("A sua idade é",idade)

linguagem1 = input('qual é a linguagem de programação que você está estudando?')
idade1 = input('Qual a sua idade?')

print("A linguagem que você está estudando é", linguagem1)
print("A sua idade é",idade1)


#mesmo conteúdo, resultados diferentes


linguagem = input('qual é a linguagem de programação que você está estudando?')
print("A linguagem que você está estudando é", linguagem)

idade = input('Qual a sua idade?')
print("A sua idade é",idade)

#mesmo conteúdo, resultados diferentes

print   ('você está estudando', linguagem, 'e sua idade é', idade)