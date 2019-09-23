def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1


def collatz_seq(n):
    seq = []
    next_num = n
    while True:
        next_num = collatz(next_num)
        seq.append(next_num)
        if next_num == 1:
            break
    return seq


longest_chain_len = 0
best_num = 0

for i in range(1, int(1e6)):
    seq = collatz_seq(i)
    if len(seq) > longest_chain_len:
        longest_chain_len = len(seq)
        best_num = i

print('Longest chain length: %s' % longest_chain_len)
print('Associated number: %s' % best_num)
