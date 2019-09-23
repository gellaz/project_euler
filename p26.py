def print_dec(num, prec):
    print("{:.{}f}".format(num, prec))


def decimal_part(num):  
    dec_part = str(num).split('.')[1]


print_dec(1/7, 50)