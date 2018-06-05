number = [1,6,8,1,2,1,5,6]
n = int(input("enter a number? "))
count = 0
for i in range(len(number)):
    if n == number[i]:
    
        count +=1
print(n, "appears",count,"times in my list")


