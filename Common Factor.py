def CommonFactor(a):
    if a == 0:
        return 0
    elif a < 0:
        a = abs(a)  
    for i in range(1,a+1):
        if a%i==0:
            print(i)

CommonFactor(15)