def is_palindrome(num):
    s = str(num)
    if len(s)%2 != 0:
        return False
    else:
        mid = int(len(s)/2)
        for i in range(mid):
            if s[i] != s[len(s)-1-i]:
                return False
    
    return True

largest = 0

for n1 in range(100,1000):
    for n2 in range(100,1000):
        product = n1*n2
        if is_palindrome(product) and product > largest:
            largest = product

print(largest)