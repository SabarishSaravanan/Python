def up_low(s):
    bracket=[]
    bracket2=[]

    for let in s:
        if let.isupper():
            bracket.append(let)
        elif let.islower():
            bracket2.append(let)
    print(s)
    print(bracket)
    r=len(bracket)
    print(f"No. of Upper case characters :  {r}")
    print(bracket2)
    p=len(bracket2)
    print(f"No. of Lower case characters :  {p}")
print("________________________________________________________________")
def unique_list(lst):
    list=[]
    for num in lst:
        if num not in list:
            return list.append(num)
print("________________________________________________________________")
def multiply(*number):
    a=1
    for num in number:
        a=a*num
    return a
print("________________________________________________________________")
def palindrome(s):
    if s[::-1]==s:
    
     return True
            
