n = int(input("N >>> "))

name = input("Escriba su nombre >>> ")
last_name = input("Escriba su apellido >>> ")

i = 1

while i <= n:
    if i % 2 == 0:
        print(last_name, end=", ")
    else:
        print(name, end=", ")
    i = i + 1