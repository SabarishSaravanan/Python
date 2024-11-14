def Automorphic(n):
    s=str(n)
    u=len(s)
    t=str(n**2)
    if t[-u:] == s:
        return True
    else:
        return False

print(Automorphic(25))