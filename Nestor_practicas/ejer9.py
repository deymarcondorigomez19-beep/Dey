n = int(input("N >>> "))
x = True
i = 0 
while i < n:
    if i % 2 == 0:
        x = not x
    if x == True:
        print("0", end=", ")
    else:
        print("1", end=", ")
    i = i + 1