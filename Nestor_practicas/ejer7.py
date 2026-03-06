n = int(input("N >>> "))
x = 1
i = 3
while i <= n + 2:
    if i % 3 == 0:
        print("a", end=", ")
        x = 1
    elif x == 1:
        print("b", end=", ")
        x = 3
    else:
        print("c", end=", ")

    i = i + 1