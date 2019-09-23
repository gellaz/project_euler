import itertools 
  
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = itertools.permutations(digits)
perm_list = list(perm)
  
for i, p in enumerate(perm_list):
    if i == 999999:
        print(i, p)
        break