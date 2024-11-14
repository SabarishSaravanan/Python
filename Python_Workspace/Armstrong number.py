def Armstrong(n):
    s=str(n)
    sum=0
    for num in s:
        sum += int(num)**(len(s))
    if n==sum:
        print("Armstrong number!")
    else:
        print("Not a Armstrong number!")
Armstrong(155)