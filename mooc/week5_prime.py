

# 输出连续N后连续5个质数
def isprime(m):
    for i in range(2,m):
        if m%i ==0:
            return False
    return True


n = eval(input("输入起始计算的个数："))
count = 0
while count<5:
    if isprime(n):
        print(n,end=" ")
        count+=1
        n+=1
    n+=1

