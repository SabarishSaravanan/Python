def Palindrome(a):
    return a==a[::-1]


#without built-in:
def Palindrome(a):
    for i in range(len(a)//2):
        if a[i]!=a[len(a)-1-i]:
            return False
    return True

    
print(Palindrome("malayala"))
print(Palindrome("malayalam"))