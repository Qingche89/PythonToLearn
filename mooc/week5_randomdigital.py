#生成5个随机N位数

import random

def genpwd(length):
    return random.randint(pow(10,length-1),pow(10,length))

length = eval(input("输入位数:"))
random.seed(17)
for i in range(5):
    print(genpwd(length))