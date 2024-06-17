    #criando listas

lista = []          #lista vazia

lista = list()      #lista vazia

lista = [int, str, float, bool]

lista_de_listas  = [10[1,2,3]]


    #indexação
lista = [24, "Jessica", 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#primeiro elemento ="0"
#último elemento = "-1"

    #slices (fatiamento)

lista = [10,50,30,40,25,60,5]

print(lista[0:3])       #print lista entre o indice 1 e 3
print(lista[3:6])       #print lista entre o indice 4 e 6
print(lista[3:])        #print lista entre o indice 4 até o final
print(lista[2:6:2])      #print lista entre o indice 3, até o 6, pulando de 2 em 2
      
    #interações com for

for elemento in lista:  #percorre por cada elemento da lista
    print(elemento)

print ('comprimento da lista:', len(lista))     #demonstra quantos elementos tem na lista

for i in range(len(lista)):
    print(i)        #="print(lista[i])"



    #append

lista = [ 1 , 3 , 12 , 8 , 2 ]

print("Antes do append", lista)

lista.append(3)         #adicionar elemento ("3") ao final da lista

print("Depois do append", lista)

    #insert

lista.insert(2,10)      #adiciona o elemento ("10") ao indice ("2")

print("Depois do insert", lista)

    #extend

lista2 = [1,2,3]

lista.extend(lista2)    #adiciona elementos de uma nova lista ao final da lista original

print("Depois do extend:", lista)

    #pop

lista.pop()             #remove o ultimo elemento

print("Lista após o pop:", lista)   

lista.pop(0)            #remove o elemento do indice escolhido

print("Lista após o pop:", lista)   

    #remove

lista.remove(3)         #remove o elemento escolhido

print("Depois do remove:", lista)

    #count

print("Quantidade de 2 na lista", lista.count(2))

    #index

print("Índice do elemento 12:", lista.index(12))

    #sort

lista.sort             #ordena de forma crescente

print("Em ordem crescente", lista)

lista.sort(reverse=True)    #ordena de forma decrescente

print("Em ordem decrescente", lista)

    #Funções para listas

#len

print("Conta quantos elementos tem na lista", len(lista))

#sum

print("Soma de todos os elementos da lista", sum(lista))

#max 

print("Maior elemento da lista", max(lista))

#min

print("Menor elemento da lista", min(lista))
