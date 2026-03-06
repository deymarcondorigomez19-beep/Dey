n = int(input(">>> "))
i = 1
while i <= n:
    if i % 2 == 0:
        print("1" , end=", ")
    else:
        print("0", end=", ")
    i = i + 1