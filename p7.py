def is_prime(num):
    """
    Check if the input number is prime, i.e.
    a natural number greater than 1 that cannot
    be formed by multiplying two smaller natural
    numbers

    :param num: input number to check if it is prime
    :return: True if num is prime, False otherwise
    """
    # 1 is not considered a prime number
    if num == 1:
        return False

    # Counter to store how many numbers in the
    # range [1,num] gives zero in the modulo operation
    # with num
    cnt = 0

    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    if cnt > 2:
        return False

    return True


# List to store the prime numbers found
primes = []
# Limit where to stop calculating prime numbers
LIMIT = 10001

num = 1

while True:
    if is_prime(num):
        primes.append(num)

    if len(primes) == LIMIT:
        break

    num += 1

print(primes[-1])
