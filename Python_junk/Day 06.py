bucket=[]
def old_macdonald(name):
    if len(name)>3:
        words=name.split()
        for word in words:
            res=word[0].capitalize() +word[1:4]+ word[4].capitalize()+word[4:]
            bucket.append(res)
    else:
        print("give words more than 3")
    return str(bucket)
print("_____________________________________________________________________________________________________________")
buc=[]
def master_yoda(text):
    words=text.split()
    #for word in words:
    #    buc.append(word[::-1])
    # return buc
    return ''.join(words[::-1])
print('----------------------------------------------------------------')
def almost_there(n):
    if (n in range(1, 11)) or (n in range(100, 201)):
        return True
    else:
        return False
print('----------------------------------------------------------------')
def paper_doll(text):
    text.split()
    for i in text:
        a=(i*3)
        return ''.join(a)
print('----------------------------------------------------------------')
def print_big(letter):
    if letter == 'A':
        return "  *  \n * * \n*****\n*   *\n*   *"
    elif letter == 'B':
        return "**** \n*   *\n**** \n*   *\n**** "
    elif letter == 'C':
        return " *** \n*    \n*    \n*    \n *** "
    else:
        return "Letter not supported"

letter_input = input("Enter a letter (A, B, or C): ").upper()
output = print_big(letter_input)
print(output)
