#Python 习题  from CSDN
#Python程序题及答案分析


#1
#遍历特殊数字
for i in range(1,5):
    for j in range(1,5):
        for q in range(1,5):       #range  表示遍历
            if   (i!=j and j!=q and q!=i):  #and 表示并且
                print(i,j,q)



#2
#检测数字特性
import math
for i in range(1,1000):  #range()函数产生一个计数序列
       x=math.sqrt(i+100)
       y=math.sqrt(i+268) 
       if ((x%int(x))==0)and ((y%int(y))==0):  #判断一个浮点数是否值是个整数
           print (i)
           
#3
#闰年检测
riqi = str(input('输入年份日期：'))          #输入input函数
year = int(riqi[0:4])
month = riqi[4:6]
date =riqi[6:]
print ("year",year,"month",month,"day",date)

sum = 0

if (year%4 == 0  and year%100 !=0 ) or (year%400 ==0):#判断闰年
   daynum =[31,29,31,30,31,30,31,31,30,31,30,31]
   for i in range(int(month)-1):
              sum = sum + daynum[i]
print('天数为',sum+ int(date))



#4
#数组排序
x = int(input('输入第1个数：'))
y = int(input('输入第2个数：'))
z = int(input('输入第3个数：'))
shuzu = [x,y,z]
shuzu.sort()  #列表排序
for i in range(len(shuzu)):  #列表长度
   print(shuzu[i])
   
   
#5
#设计斐波那契数列
def fib(x):             #函数递归即是对自身的调用  特征：1计算过程存在递归链条 2存在一个不需要再次递归的基例 利用函数和分支结构实现
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

for i in range(20):
    print(fib(i),end=" ")
    
    
#6
#遍历特殊数字 水仙花数  然后排序  顺序遍历法
shuixianh = list()
for i in range(1,9):
   for j in range(9):
      for q in range(9):
           if pow(i,3)+pow(j,3)+pow(q,3) == 100*i + 10*j + q:
               shuixianh.append(100*i + 10*j + q)
shuixianh.sort()
print(str(shuixianh).replace(" ",'').strip("[").strip("]"))              

#7
#求和
a  = eval(input("输入数字："))
b  = eval(input("输入数字："))
print(a+b)

#8
#开方
a  = eval(input("输入数字："))
print(pow(a,0.5))

#9
#检测数字特性
a  = eval(input("输入数字："))
if a>0:
    print("大于")
elif a==0:
    print("等于")
else:
    print("小于")

#10
#检测数字特性
a  = eval(input("输入数字："))
if len(str(a))==3:
   ge = a%10
   shi =int((a/10) %10)
   bai = int((a/100)%10)
   print(a,ge,shi,bai)
   if (ge**3 +shi**3 + bai**3) == a:
       print("ok")

#11
#素数质数求和
def isprime(x):
    num=0
    for c in range(1,x+1):
        if (  x%c == 0):
            num+=1
    if  num>2:
         return False
    else:
         return True
         
a = int(input("输入范围："))
for i in range(1,a):
    if(isprime(i)):
         print(i)

#12
#打印月历
import calendar                   # 引入日历模块
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
print(calendar.month(yy,mm))

#13
#统计英文空格数字等
str=input("请输入一个字符串:")
print(str)
letters = 0
space = 0
digit = 0
others = 0
for c in str:
   if c.isalpha():           #字符操作
         letters += 1
   elif c.isspace():           
         space += 1
   elif c.isdigit():
         digit += 1
   else:
         others += 1
print("字符串共有%d个英文字母，%d个空格，%d个数字，%d个其他字符"%(letters,space,digit,others))

#14
#输入转化大写  读写文件
str = input('输入字符串:')
str = str.upper()
fp = open('creat/test.txt','w+')  #创建或打开 读写
fp.write(str)
fp = open('creat/test.txt','r')
print(fp) # <_io.TextIOWrapper name='creat/test.txt' mode='r' encoding='cp936'>
print(fp.read())
fp.close()

#15
#数制转化  异常处理
try:
    dec = int(input("输入数字："))
except  ZeroDivisionError as err :
    print("零除错误:{}".format(err))
except (ValueError) as err:
    print("取值错误,输入必须为数字:{}".format(err))
except:
    print("Unexpected error!")#raise
else:         
    print("0b二进制为：{}".format(bin(dec)))
    print("0o八进制为：{}".format(oct(dec)))
    print("0x十六进制为：{}".format(hex(dec)))
finally:
    print("程序结束")
    
    
#16
#随机素数
import random as rm 
def isprime(x):
    num=0
    for c in range(1,x+1):
        if (  x%c == 0):
            num+=1
    if  num>2:
         return False
    else:
         return True

pl = list()
for i  in range(10,100):
    if isprime(i):
        pl.append(i)

count =0
while count<10:
    print(pl[rm.randint(0,len(pl)-1)]   ,end=",")
    count+=1