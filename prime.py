def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0: 
                return False
        else:
            return True
    else:
        return False

def primes_range(l_bound, u_bound):
    return [n for n in range(l_bound, u_bound + 1) if is_prime(n)]