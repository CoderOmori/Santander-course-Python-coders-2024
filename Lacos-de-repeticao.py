            # > While

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20"))

while numero_sorteado != numero_escolhido:
    print("Você errou, tente novamente")

    numero_escolhido = int(input("Informe um número entre 1 e 20"))
 
print ("Parabéns, você acertou")

    # > Estrutura com contador

contador = 0

while contador < 5: 
    print(contador)

contador = contador + 1
       
            # For

for variavel in range(10):      #para variavel dentro da faixa (x) (menor do que(x))
    print(variavel)
    

for variavel in range(1, 11):
    print(variavel)

for variavel in range(1, 12, 3):
    print(variavel)

#
    
nota1 = float(input("Informe sua nota 1:"))
nota2 = float(input("Informe sua nota 2:"))
nota3 = float(input("Informe sua nota 3:"))


soma= 0

for i in range (1,4):
    nota = float(input(f"Informe a sua nota (i):"))

    soma = soma + nota

print(soma/3)