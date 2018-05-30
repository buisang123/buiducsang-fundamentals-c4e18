menu = ['T-shirt','ao len']
loop = True
while loop:
    n = input('chao ban. ban muon gi (C,R,U,D)? ')
    
    if n == 'R':
        print('cac mat hang cua chung toi:',*menu,sep=',')
    elif n == 'C':
        m = input('nhap mat hang moi: ')
        menu.append(m)
        print('mat hang cua chung toi: ',*menu,sep=',')
    elif n == 'U':
        z = int(input('cap nhat vi tri? '))
        b = input('mat hang moi ? ')
        menu[z-1] = b
        print(*menu,sep=',')
    elif n == 'D':
        k = int(input('xoa vi tri? '))
        menu.pop(k-1)
        print(*menu,sep=',')
    elif n == 'Q':
        loop = False
