def Armstrong_range(a,b):
    for num in range(a,b+1):
        s=str(num)
        sum=0
        for i in s:
            sum=sum+int(i)**(len(s))
        if sum == num:
            print(num)

Armstrong_range(1,10000)

