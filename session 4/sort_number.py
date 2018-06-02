menu = [10,2,-5,4]
print(*menu,sep=', ')
sort = []

while True:
    n = min(menu)
    sort.append(n)
    menu.remove(n)
    if len(menu) == 0:
        break
print(*sort)