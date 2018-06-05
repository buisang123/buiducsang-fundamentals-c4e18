person = {'hc':'hoc','ng':'nguoi','eny':'em nguoi yeu','lm':'lam','ns':'noi'}
while True:
    for k in person:
        print(k,end="\t")
    print()
    n = input("your code?, ")
    if n in person:
        print("traslation",person[n])
    else:
        print("not found")
        user_choice = input("do you want to contribute")
        if user_choice == 'Y':
            translation = input('your ')
            person[n]=translation
        else:
            print("bye")
            break

    