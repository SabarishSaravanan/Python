def digits(k):
    n = str(k)   
    count = 0  
    for i in range(len(n)):
        if n[i] == "0":
            count += 1
        else:
            break  
    n=n[i:]
    print(len(n))  

digits(74545454)
