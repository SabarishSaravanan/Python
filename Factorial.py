def factorial(n):
    fact=1
    if n==0:
        print(1)
    else:
            for num in range(1,n+1):
                fact=fact*num
            print(fact)

factorial(10)