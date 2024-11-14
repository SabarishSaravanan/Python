def gcd(a,b):
    if a == 0:
        return b 
    if b == 0:
        return a
    smaller=min(a,b)
    for num in range(smaller,0,-1):
        if a%num == 0 and b%num == 0:
            return num
            
def lcm(a,b):

    c=a*b
    if a>0 and b>0:
         lcm= c//gcd(a,b)
         return lcm
   

print(lcm(10,16))
