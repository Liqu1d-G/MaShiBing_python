# Editor : Liquid
# Time :  15:56

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(6))  # 8  斐波那契数列中第六个数
