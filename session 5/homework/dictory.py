prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3


}
stock = {
"apple": 0,
"banana": 6,
"orange": 32,
"pear": 15


}
tong = 0
for k,v in stock.items():
    print()
    print(k)
    print("stock:",stock[k])
    print("price:",prices[k])
    zero = stock[k]*prices[k]
    print('=',zero)
    tong += zero
print("total= ",tong)

