def even(list):
    evenList=[]
    oddList=[]
    for num in list:
        if num%2==0:
            evenList.append(num)
        else:
            oddList.append(num)
    tuple=(oddList,evenList)
    return tuple


