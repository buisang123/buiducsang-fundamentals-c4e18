menu = [5,7,300,300,24,50,75]
print("hello,my name is Hiep and there are my ship size: ")
print( *menu,sep=', ' )
print('now my biggest shep has size ',max(menu)," let's shear it ")
n = max(menu)
 
while True:

    print('after shearing, here is my lock ')
    for i in range(len(menu)):
        if menu[i] == n:
            menu[i] = 8
    print(*menu,sep=', ') 
    print('one month has passed, now here my flock') 
    for item in menu:
        print(item + 50, end=", ")



# menu[menu.index(max(menu))] = 8