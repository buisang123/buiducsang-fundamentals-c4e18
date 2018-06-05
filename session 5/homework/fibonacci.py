def F(n):
    if n == 0:
         return 1
    elif n == 1:
         return 2
    else: return F(n-1)+F(n-2)
for i in range(5):
    print("month " "{0}: {1}"" paie(s) of rabbit".format(i,F(i)))
