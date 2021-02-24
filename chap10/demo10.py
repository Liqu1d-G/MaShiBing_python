# Editor : Liquid
# Time :  15:54


def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)


print(fac(6))  # 720
