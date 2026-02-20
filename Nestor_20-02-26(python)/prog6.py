a = int(input("> "))
b = int(input("> "))

print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")

op = int(input("> "))

if(op == 1):
    print(a + b)
if(op == 2):
    print(a - b)
if(op == 3):
    print(a * b)
if(op == 4):
    print(a / b)

