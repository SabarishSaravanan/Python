def binary_to_decimal(binary):
    Bin= str(binary)
    decimal = 0
    power=0
    for num in reversed(Bin):
        decimal= decimal+(2**power)
        power=power+1
    print(decimal)

binary_to_decimal(11111111)
