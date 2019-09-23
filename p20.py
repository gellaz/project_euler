def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

num = factorial(100)
digits = list(map(int, str(num)))
print(sum(digits))