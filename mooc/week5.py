# M-5：函数和代码复用
# M-5
# 函数 是否为素数
def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


sum = 0
for i in range(1, 100):
    if isprime(i):
        sum += i
        print(i)
print("100以内素数的和为：" ,str(sum) )


n = eval(input("输入素数的范围："))
ls = []
count = 0
while count < 6:
    if isprime(n):
        ls.append(n);
        count += 1
    n += 1
print("{},{},{},{},{}".format(ls[0], ls[1], ls[2], ls[3], ls[4]))


# M-5
# 代码复用
# 引入PyInstaller第三方库  需要联网安装  将.py打包成编译好的可执行文件
# 安装使用 cmd命令行 pip install pyinstaller 联网下载安装
# cmd pyinstaller -i XXX.cio  -F  XXX.py  其中 -i为图标 -F为只生成一个文件