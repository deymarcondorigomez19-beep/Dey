n = int(input("N >>> "))
x = int(input("X >>> "))
i = 1 
while i <= n:
    if i % 2 == 0:
        print("0", end=", ")
    else:
        print(x , end=", ")
    i = i + 1