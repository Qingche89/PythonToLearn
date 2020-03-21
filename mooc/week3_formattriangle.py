# 格式化输出三角
n = eval(input("输入三角的阶数："))
for i in range(n):
    print("{0:^{1:}}".format((2*i+1)*'*',2*n-1))