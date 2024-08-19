def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    if n < r:
        return 0 

    numerator = factorial(n)
    denominator = factorial(n - r)
    perm = numerator // denominator
    print(perm)

permutation(5, 1)  
