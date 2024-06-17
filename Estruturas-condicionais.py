# > Estruturas condicionais

idade = 18

if idade >- 18:         #se a idade for igual ou maior que 18, então

    print("Você é maior de idade.")

else:                   #do contrário
    print("Você é menor de idade.")




#

media = float(input("Adicione a média aqui:"))

if media >= 6:
    print ("Você foi aprovado")

elif media >= 5:        #ou então
    print ("Recuperação")      

else:
    print ("Você não foi aprovado")
    
    #

media1 = float(input("Adicione a média1 aqui:"))
presenca = float(input("Adicione o percentual de presença aqui:"))

if media1 >= 7 and presenca >= 70:      #Se a média1 é igual ou maior que 7 e a presençã maior ou igual a 70, então
    print("Aprovado")
else:
    print("Reprovado")