n = int(input("N >>> "))
x = 0
i = 1 
while i <= n:
    if i % 3 == 0:
        print(x, end=", ")
        x = 0
    else:
        print(x, end=", ")
        x = x + 1
    i = i + 1