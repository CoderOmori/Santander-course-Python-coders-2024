x = 4.2

y = 10

z = "42"

not (((x * y == z) and not (x < y)) or y % 2 == 0)



#alternativa 01
not (not (x < y and x * y == z)) or (x >= y or y % 2 == 0)

#alternativa 02
not False

#alternativa 03
not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z)))))

#alternativa 04
not (((not True) or int(z) % 7 == 0) and ((str(int(x*y)) == z) and (type(x) != type(z))))

#alternativa 05
(True and True) or not True