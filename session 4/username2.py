username = input("username: ")
loop = True
count = 0
while loop:
   
    if count <= 4:
        print('you are no superruser')
        loop = False
    
    elif username == "sang":
        password = int(input("passwork: "))
        if password == '123456':
            print ("welcome ce4")
            break    
    
   

    