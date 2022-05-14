#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)


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
with open('products.csv', 'w', encoding = 'utf-8') as f: #encoding用了utf-8才不會亂碼
	f.write('商品,價格\n') #用逗號區隔!!
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #用逗點可讓content在不同的CSV格子裡 

