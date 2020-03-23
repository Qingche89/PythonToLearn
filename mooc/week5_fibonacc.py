#递归实现斐波那契数列

def fbi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbi(n - 1) + fbi(n - 2)


n = eval(input("输入序列个数："))
for i in range(1,n+1):
    print(fbi(i),end=",")