a = int(input("ingrese un numero > "))
b = int(input("ingrese un numero > "))
c = int(input("ingrese un numero > "))

may = a
if(b > may):
    may = b
if(c > may):
    may = c
print("el numero mayor es: " + str(may))
