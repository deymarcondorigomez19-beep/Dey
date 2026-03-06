n = int(input("N >>> "))
x = 1
i = 1 
while i <= n:
    if i % 4 == 0:
        print(x, end=", ")
        x = 1
    else:
        print(x, end=", ")
        x = x + 1
    i = i + 1

# pudo haberse hecho mas simple