for i in range(2,101):
    a = 0
    for j in range(2,i):
        r = i%j
        if(r == 0):
            a = 1

    if(a == 0):
        print(i)