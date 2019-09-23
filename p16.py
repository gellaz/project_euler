def get_sum_of_digits(pow):
    num = 2**pow
    return sum(list(map(int, str(num))))


print(get_sum_of_digits(1000))
