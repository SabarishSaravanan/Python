def Xdigit(x, n):
    count = 0
    x = str(x)  
    for num in range(n + 1):
        s = str(num)  
        count =count + s.count(x)
    print(count)


Xdigit(2, 25)