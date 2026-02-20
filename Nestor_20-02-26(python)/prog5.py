m = int(input("> "))
a = int(input("> "))

if(a<=m):
    print("compro " + str(a))
    m = m - a
b = int(input("> "))
if(b<=m):
    print("compro " + str(b))
    m = m -  b
c = int(input("> "))
if(c<=m):
    print("compro " + str(c))
    m = m -  c
print("saldo: " + str(m))
