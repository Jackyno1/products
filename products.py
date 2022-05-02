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

#加入write功能
with open('products.csv', 'w') as f: #用逗點可讓content在不同的CSV格子裡
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

