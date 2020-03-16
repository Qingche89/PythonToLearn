# -*- coding: utf-8 -*-
#嵩天老师的python123上的课后练习


#M-1
#表达式运算  M OP N
#eval()  估值函数的神奇妙用
a = input("")
res = eval(a)
print("{:.2f}".format(res))

#汉字大小写转换
#数组/列表的有序性妙用
template = "零一二三四五六七八九"
s = input()
for i in s:
    print(template[eval(i)], end="")

#M-2
#输出叠边花
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(100)
    t.left(80)
t.done()


#M-3
#格式化输出三角矩阵
n = eval(input("输入三角矩阵的阶数："))
for i in range(n):
    print("{0:^{1:}}".format((2*i+1)*'*',2*n-1)) #格式化输出三角



#M-4
#遍历特殊数字 水仙花数  自增遍历法
sum =""    
for i in range(100,1000):
     if  int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3  == i:
         sum += str(i) + ","
print(sum[0:-1])        



#M-4
#用户登录的三次机会
#运用while进行非确定次数循环
count = 0
#message = ""
while count < 3:
    username = input("输入用户名:")
    password = input("输入密  码:")
    if username == "Kate" and password == "666666":
          message = "登录成功！"
          break
    else:
          print("用户名或密码错误请重新输入!")
          count+=1
          if count ==3:
              message = "3次用户名或者密码均有误！退出程序。"
print(message)           
  










#M-7
#读取文件，计算平均每行多少字
file = open("../data/latex.log","r")
zishu = 0 
hangshu = 0
for line in file:
    reall = line.strip("\n")
    if  reall != "":
       hangshu+=1
       zishu += len(reall)

print(round(zishu/hangshu))
file.close()



#读CSV,然后操作
f = open("../data/data.csv","r")
line  = f.readlines()
line = line[::-1]

for x in line:
    x=x.replace(" ",'')   #去换行，去空格
    x=x.strip("\n")       #去换行，去空格
    x=x.replace(",",";")
    x= x[::-1]
    print(x)