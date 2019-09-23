sum_of_the_squares = 0
for num in range(1, 101):
    sum_of_the_squares += num ** 2

square_of_the_sum = sum(n for n in range(1, 101)) ** 2

diff = square_of_the_sum - sum_of_the_squares
print(diff)
