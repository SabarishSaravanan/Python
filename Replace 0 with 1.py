def replace0(n):
    s=str(n)
    lis=list(s)
    print(lis)
    for i in range(len(s)):
        if lis[i]=='0':
             lis[i]='1'
    print(lis)
    a=int(''.join(lis))
    print(a)
    print(type(a))
replace0(456002) 