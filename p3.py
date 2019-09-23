num = 600851475143

def is_prime(num):
    temp = num // 2 + 1
    for n in range(2,temp):
        if num%n == 0:
            return False
    return True

t = num // 2 + 1
for i in range(1,t):
    if num%i==0 and is_prime(i):
        print(i)
