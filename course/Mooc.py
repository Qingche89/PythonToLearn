#M  Python基础语法框架  不涉及面向对象编程
#跟随嵩天老师团队学习  北京理工大学


#M-1:python基础语法元素
#M-1
#Python温度转换实例
'''
      奋斗的人生不需要过多的解释
''' #多行注释
wendu  = str(input('输入温度：'))
#if wendu[-1] == 'F':  #正0/逆-1向序号  索引或者切片：   列表[] 或 元组()
if wendu[-1] in ['f' , 'F']:            # if in   和  while in 
   #print("摄氏温度为",(int(wendu[0:-1])-32)/1.8,'C')
    c = (eval(wendu[0:-1])-32)/1.8       #eval评估函数  去最外侧引号并执行之
    print("华氏温度{:.2f}F摄氏温度为{:.2f}C".format(eval(wendu[0:-1]),c))     #格式化输出方法 写出带槽的模板字符串"{0:引导 .2精度 f%类型}{0:}{0:}{2:}".format(a,b,c)
elif wendu[-1] in ['C' , 'c']:      #elif<条件>：   elif
   print("华氏温度为",int(wendu[0:-1])*1.8+32,'F')
else:
  print("输入错误")



#M-2:python基本图形绘制  turtle库
#M-2
#基本图形绘制  闪电
import turtle  #引入海龟绘图turtle模块
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
turtle.done()



#M-3:基本数据类型
#M-3
#数字类型及操作
print("-1的绝对值",abs(-2))
print("最大值",max(1,2,3,4,5))
print("2的3次幂",pow(2,3))
x=0
x+=2
print("二元操作符的自加操作x+=2",x)
print("pi的四舍五入",round(3.1415926,2))
print("浮点数位数不确定性",0.1+0.2)
print("10//3整除",10//3)
print("10%3取余数",10%3)
print("10除3的商余函数",divmod(10,3))
print("int型转换",int(10.3331234))


#M-3
#字符串类型及操作

#字符串就是有序的字符 序列，可以索引和切片表示,（其中正0/逆-1向序号）
#字符串可以用 ' ''  '''  来表达区分
print('"abcd\nefg"的逆序',"abcd \nefg"[::-1])  #-1表示步长  \n为转义字符表示换行
print('字符串"abcd"和字符串"efg"可以拼接',"abcd"+"nefg")
print('字符串"el"可以在字符串"Hello"中搜索',"el" in "Hello")
print('可以计算在字符串"哈哈哈"的长度',len('哈哈哈'))
print('转成字符串',str(1+2))
print('python采用了Unicode编码,ord返回Unicode编码，chr返回相应字符，输出星座')
for i in range(12):
    print(chr(9800+i),end='')  #end表示不换行
print("一些字符串类的方法：abd字符串大写"+'abc'.upper()+'小写'+'GhK'.lower()+'l在hello中次数'+str("Hello".count('l')))
print('一些字符串类的方法："a,b,c"用分隔符形成元组的形式返回'+str('a,b,c'.split(",")))
print('一些字符串类的方法："abc"加上分隔符'+'|'.join('abcdefg'))





#M-4:程序的控制结构  分支  循环
#分支 if    异常try: except: else: finally 
#循环 遍历循环               for <循环变量> in <遍历结构：计数序列/range()  字符序列 for c in str  列表 for item in []  文件for line in fp>  
#     无限循环（知道条件）   while
#循环控制保留 break  continue


        
#M-5：函数和代码复用
#M-5
#函数 是否为素数
def isprime(x):
    for i in range(2,x):
        if x%i == 0 :
           return False   
    return True

sum = 0 
for i in range(1,100):
    if  isprime(i):
            sum+=i
            print(i)
print(sum, sum+1)     #多值返回return  元组(1060,1061)

      

#M-5
#代码复用
# 引入PyInstaller第三方库  需要联网安装  将.py打包成编译好的可执行文件
# 安装使用 cmd命令行 pip install pyinstaller 联网下载安装
# cmd pyinstaller -i XXX.cio  -F  XXX.py  其中 -i为图标 -F为只生成一个文件




#M-5
def prime(m):
    for i in  range(2,m):
          if m%i == 0:
               return False
    return True

n = eval(input())
ls = []
count = 0
while count<6:
   if prime(n):
          ls.append(n);
          count+=1
   n+=1
print("{},{},{},{},{}".format(ls[0],ls[1],ls[2],ls[3],ls[4]))


#M-6
#组合数据类型  包括 集合类型  序列类型：字符串"" 列表[] 元组()    字典/映射类型 

#集合类型：无序的不同元素{，，}
#运算操作符 并|  差- 交& 补^     关系比较 子集<  包含>
#方法  S.add()  remove()  clear()清空  pop()随机取走 copy()副本 len() set()转集合/初始化/可表示空
#应用集合数据去重
ls = [1,3,4,5,12,2,3,53,3,1,2]
A= set(ls)
ls = list(A)
print(ls)

#序列类型：一组有序的元素  字符串""   列表[] 元组()  序号为正向0/逆向-1  操作符  索引和切片  复制*n  连接+
#方法  len()  min() max() index() count()
#字符串"" 略
#元组()  创建初始化(，，)或，，或tuple()  多用于函数多值返回return为元组（），（）可以省略  不能被修改
#列表[]  创建初始化[]或list()  ls[i]替换 del ls[i]删除  ls.append(x)追加  ls.reverse()反转  ls.sort()排序

#字典类型   dict ={ "key":value , : , ：}   dict[key]相当于自定义的序号  空字典  dict={}  dict.get(key)   


#M-6
#jieba第三方库  中文分词
#pip install jieba

import jieba as jb
jb.add_word("宋一楠")
print(jb.lcut("宋一楠是个好人正直的人"))