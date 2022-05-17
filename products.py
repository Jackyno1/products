# 找檔案在不在
import os

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
	return products

# 讓使用者輸入
def user_input(products):
	while True:
	    name = input('請輸入商品名稱:')
	    if name == 'q': #quit
		    break
	    price = input('請輸入商品金額:')
	    products.append([name,price])
	print(products)
	return products

# add for loop
def price_tag(products):
	for p in products:
		print(p[0], '的價格為', p[1])

# 加入write功能
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f: #encoding用了utf-8才不會亂碼
		f.write('商品,價格\n') #用逗號區隔!!
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #用逗點可讓content在不同的CSV格子裡 

def main():			
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! 找到檔案了')
	else: 
		print('找不到檔案....')
	products = read_file(filename)
	products = user_input(products)
	price_tag(products)
	write_file(filename, products)

main()