def Month(m, y):

    is_leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    
    months_31 = [1, 3, 5, 7, 8, 10, 12]

    months_30 = [4, 6, 9, 11]
    
    if m < 1 or m > 12:
        print("Invalid month")
    elif m == 2:
        print("29 days" if is_leap else "28 days")
    elif m in months_31:
        print("31 days")
    elif m in months_30:
        print("30 days")

Month(9, 2024) 