def divisors(number):
    divs = [i for i in range(1, number//2) if number%i == 0]
    return divs

print(sum(divisors(10000)))