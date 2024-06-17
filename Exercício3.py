x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)


#print(num == x, num == y, num == x + y)        #True False False

#print(2 == "2", False, 2.0 == 2)                #False False True

#print(True, False, False)                       #True False False

print(num == x*y, num*y == x*y, y > x + num)

#print(False, True, True)                        #False True True