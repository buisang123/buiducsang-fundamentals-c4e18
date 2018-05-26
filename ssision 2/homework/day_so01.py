# for i in range(6):
#     print("1 0", end = " ")
# print()

n = int(input("enter the total number 1's and 0's : "))

for i in range(n):
    if i % 2 == 0:
        print("0", end= " ")
    else:
        print("1", end= " ")

    