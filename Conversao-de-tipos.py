# Conversão de tipos

idade = '24'
numero1 = '10'
numero2 = '20'

print(numero1 + numero2)

'print(10+idade)'             #erro na operação 'int' + 'str'

print(idade,type(idade))      #class str

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

#int(): converte em inteiro
#str(): converte em string
#float(): converte em float
#bool(): converte em booleano

# altura = (input ('Informe a sua altura:)          #recebe a resposta em str

  altura = float (input ('Informe a sua altura:'))  #converte a resposta em float

print(altura,type(altura))
