# -*- coding: utf-8 -*-


#蒙特卡罗法计算圆周率


import random as rm     #引入random随机标准库  标准库无需安装
import time 

rm.seed(123)             #引用随机数种子，若不引用则以系统的时间为种子，导致程序无法重现
#print(rm.random())   
#print(rm.randint(20,100))

count = eval(input("输入运算次数:"))

hits = 0
start = time.perf_counter()
for i in range(1, count+1):
    x, y = rm.random(), rm.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        hits = hits + 1
pi = 4 * (hits/count)        #采用工程学上的蒙特卡洛法散点计算权重近似的求解
print("圆周率值是: {:.6f}".format(pi))
print("运行时间是: {:.5f}s".format(time.perf_counter() - start))