#basket=[]
#def myfunc(string):
#   words=string.split()
#   for word in words():
#      if word=="o":
#         word.upper()
#        basket.append(word)
#   else:
#      basket.append()
basket = []

def myfunc(string):
    words = string.split()  # Split the input string into words
    for word in words:
        if word == "o":
            basket.append(word.upper())  # Append uppercase "O" to the basket
        else:
            basket.append(word)  # Append other words to the basket

    return basket

result = myfunc(string)
print(result)
