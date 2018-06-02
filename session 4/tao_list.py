n = input()
s = n.split()
numb = []
for item in s:
    numb.append(int(item))
print(*numb)