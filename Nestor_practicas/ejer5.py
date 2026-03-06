n = int(input("N >>> "))
i = 3
while i <= n + 2:
    if i % 3 == 0:
        print("1", end=", ")
    else:
        print("0", end=", ")
    i = i + 1