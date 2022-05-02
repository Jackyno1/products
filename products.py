products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q': #quit
	    break
    price = input('請輸入商品金額:')
    products.append([name,price])
print(products)

#add for loop
for p in products:
	print(p[0], '的價格為', p[1])

