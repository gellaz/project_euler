def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)

def fibonacci_seq(num):
    seq = []
    for n in range(num+1):
        seq.append(fibonacci(n))
    
    return seq

def fibonacci_limited_seq(lim):
    seq = []
    n = 0

    while True:
        elm = fibonacci(n)

        if elm > lim:
            break
        
        seq.append(elm)
        n += 1
    
    return seq

seq = fibonacci_limited_seq(4000000)
tot = 0
for n in seq:
    if n%2 == 0:
        tot += n

print(tot)

