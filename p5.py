def is_div(num, ran):
    """
    This function check if a number is
    divisible from all the number in the 
    range [1,ran]

    :param num: number to check
    :param ran: range of dividends
    :return: True if num is divisible from
        all the numbers in that 
    """
    for i in range(1, ran+1):
        if num % i != 0:
            return False

    return True


num = 20

while True:
    if is_div(num, 20):
        res = num
        break
    num += 1

print(res)
