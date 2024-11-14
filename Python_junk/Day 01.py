st = 'Print only the words that start with s in this sentence'
print(st.split())
for word in st.split():
    if word[0]=="s":
        print(word)
    pass
print("*******************************")

list=[x for x in range(1,50) if x%3]
print(list)

print("*******************************")



st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word)
    continue

print("*******************************")

for num in range(1,16):
    if num%3==0 and num%5==0:
        print("bizbuz")
    elif num%3==0:
        print("biz")
    elif num%5==0:
        print("buz")
    else:
        print(num)

print("*******************************")

st = 'Create a list of the first letters of every word in this string'
list=[x[0] for x in st.split()]  
print(list)



print("*****************   THE END DA THAMBU!    ***************************")
