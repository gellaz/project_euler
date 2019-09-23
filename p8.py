def is_pyt_triplet(a, b, c):
    """
    Checks if the three natural numbers a, b and c form
    a pythagorean triplet, i.e. if they meet the
    following conditions:
        (1) a < b < c
        (2) a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    :param a: first number of the triplet
    :param b: second number of the triplet
    :param c: third number of the triplet
    :return: True if the three numbers form
         a pythagorean triplet.
    """
    c1 = (a < b and b < c)
    c2 = (a**2 + b**2 == c**2)

    if c1 and c2:
        return True

    return False


def sum_1000(a, b, c):
    """
    Checks if three numbers summed up together
    have 1000 as a result.

    :param a: first number
    :param b: second number
    :param c: third number
    :return: True if the sum is 1000, False otherwise
    """
    return (a + b + c) == 1000


for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if is_pyt_triplet(i, j, k) and \
                    sum_1000(i, j, k):
                print('i:%s\nj:%s\nk:%s' % (i, j, k))
                break
