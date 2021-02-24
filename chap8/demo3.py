# Editor : Liquid
# Time :  19:09


t = (9, [20, 30], 10)

print(t)  # (9, [20, 30], 10)

t[1].append(100)
print(t)  # (9, [20, 30, 100], 10)

# t[1] = 100  # TypeError: 'tuple' object does not support item assignment
