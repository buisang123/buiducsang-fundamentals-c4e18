n = int(input('enter a number: '))
prime = True

for i in range(2,n):
    if (n % i == 0 ):
        prime = False
        break
if prime:
    print('{0} is a not a prime number'.format(n))
else:
    print('{0} is a not a prime number')

