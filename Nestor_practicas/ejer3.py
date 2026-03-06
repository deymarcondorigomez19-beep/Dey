n = int(input("N >>> "))
a = int(input("A >>> "))
b = int(input("B >>> "))
i = 1 
while i <= n:
    if i % 2 == 0:
        print(b, end=", ")
    else:
        print(a, end=", ")
    i = i + 1