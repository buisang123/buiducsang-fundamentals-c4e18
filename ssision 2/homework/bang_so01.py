for i in range(9):
    if i % 2 == 0:
        for j in range(9):
            if j % 2 == 0:
                print("1",end= " ")
            else:
                print("0",end= " ")
            
              
    else:
        for j in range(9):
            if j % 2 == 0:
                print("0",end= " ")
            else:
                print("1",end= " ")
    print()


n = int(input("enter a number: "))
for a in range(n):
    if a % 2 == 0:
        for b in range(n):
            if b % 2 == 0:
                print("1",end= " ")
            else:
                print("0",end= " ")
    else:
        for b in range(n):
            if b % 2 == 0:
                print("0",end= " ")
            else:
                print("1",end= " ")
    print()
                
       
        

