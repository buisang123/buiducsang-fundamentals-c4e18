from random import choice, shuffle
menu = []
work = "champion"
chair = list(work)

shuffle(chair)
print(' '.join(chair))

print(*menu,end=' ')
loop = True
while loop:
    n = input('your answer: ')
    if n == work:
        print('HURA :V')
        loop = False
    else:
        print('sai roi')

    