n = int(input("n>>"))
x = int(input("x>>"))

for i in range(1, n*x+1, 1):
    if i % x == 0:
        print(i)