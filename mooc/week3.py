




#W-3:基本数据类型

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


#引入math标准库
import math
print(math.pi , math.e)
print(pow(4,0.5))  #开方

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
