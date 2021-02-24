# Editor : Liquid
# Time :  19:28


s1 = {10, 20, 30}
s2 = {20, 40, 50}

print(s1.intersection(s2))  # {20}  求交集
print(s1 & s2)  # {20}  求交集


print(s1.union(s2))
print(s1 | s2)  # {50, 20, 40, 10, 30}  求并集

print(s1.difference(s2))
print(s1 - s2)  # {10, 30}  求差集

print(s1.symmetric_difference(s2))
print(s1 ^ s2)  # {40, 10, 50, 30}  求对称差集


