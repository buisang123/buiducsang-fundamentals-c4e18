s = 'ThiS is String with Upper and lower case Letters'

counts = {}
for c in s.lower():
    counts[c] = counts.get(c,0) + 1

for c, n in sorted(counts.items()):
    print(c, n)

