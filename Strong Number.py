def factorial(n):
    fact=1
    if n==0:
        return 1
    else:
            for num in range(1,n+1):
                fact=fact*num
            return fact
        
def strong(n):
    s=str(n)
    sum=0
    for num in s:
        indfact=factorial(int(num))
        sum+=indfact
    if sum==n:
        print("It is strong number!")
    else:
        print("No, it is not!")

strong(143)