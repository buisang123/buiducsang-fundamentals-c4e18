from random import randint
numb = randint(0,100)
print(numb)
loop = True
count = 0
while loop:
    if count >= 7:                      # nguoi nhap 7 lan thi ket thuc
        print("you lose :<")
        loop = False
    else:
        n = int(input("enter a number: "))
        if n == numb:
            print("bingo :v ")
            loop = False
        elif n < numb:
            print("so nay nho hon r :( ")

        else:
            print("so nay lon hon r :( ")
    count += 1                            
    