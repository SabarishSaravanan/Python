#Maximum number of handshakes 
def Handshake(n):
    handshakes= ((n-1)*n)//2
    return handshakes
print(Handshake(5))