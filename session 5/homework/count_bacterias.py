n = int(input("how many bacterias are there? "))
m = int(input("how much time in minutes will we wait? "))
dem = m/2
while dem != 0:
    n *= 2
    dem -= 1
print("after",m,"minutes, we would have",n,"bacterias")