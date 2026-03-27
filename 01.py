x = int(input(">"))
while x != 0:
    may = 0   
    men = 10
    c= 0
    while x > 0:
        
        c = x%10
        x = x//10

        if c > may:
            may = c
        if c < men:
            men = c
    print(may, men)
    x = int(input(">"))