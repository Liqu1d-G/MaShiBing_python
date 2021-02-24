# Editor : Liquid
# Time :  17:45


# 字典生成式

# 若二者元素数量不同，则以少的那个为准

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

d = {item.upper(): price for item, price in zip(items, prices)}  # upper将字母大写
print(d)  # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}
