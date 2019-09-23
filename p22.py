def score(name):
    pts = [ord(c) - 64 for c in name]
    return sum(pts)

file = open('p022_names.txt', 'r')
names_str = file.readline()
names = names_str.split(',')
names = list(map(lambda s: s.replace('"', ''), names))
names = sorted(names)

tot = 0

for idx, name in enumerate(names):
    tot += (idx+1) * score(name)

file.close()

print(tot)