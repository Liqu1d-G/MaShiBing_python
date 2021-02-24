# Editor : Liquid
# Time :  19:22

s1 = {10, 20, 30, 40}
s2 = {40, 50, 60, 70}
print(s1 == s2)  # False

s3 = {20, 30, 10, 40}
print(s1 == s3)  # True

s4 = {10, 20}
print(s4.issubset(s1))  # True s4是否是s1的子集
print(s1.issuperset(s4))  # True s1是否是s4的超集

print(s2.isdisjoint(s1))  # False s1和s2是否有交集
