print('now think of a number from 0 to 100 , then press')
low = 0
high = 100
while True:
    mid = (low + high)//2
    ans = input('is {0} your number ?'.format(mid)).lower()
    if ans == "s":
        low = mid
    elif ans == 'l':
        high = mid
    elif ans == 'c':
        print('i knew it')
        break

