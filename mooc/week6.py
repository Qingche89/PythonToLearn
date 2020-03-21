#W-6:组合数据类型  包括 集合类型  序列类型：字符串"" 列表[] 元组()    字典/映射类型

#集合类型：无序的不同元素{，，}
#运算操作符 并|  差- 交& 补^     关系比较 子集<  包含>
#方法  S.add()  remove()  clear()清空  pop()随机取走 copy()副本 len() set()转集合/初始化/可表示空
#应用集合数据去重

#序列类型：一组有序的元素  1字符串""  2列表[] 3元组()  序号为正向0/逆向-1  操作符  索引和切片  复制*n  连接+
#方法  len()  min() max() index() count()
#1 字符串"" 略
#2 元组()  创建初始化(，，)或，，或tuple()  多用于函数多值返回return为元组（），（）可以省略  不能被修改
#3 列表[]  创建初始化[]或list()  ls[i]替换 del ls[i]删除  ls.append(x)追加  ls.reverse()反转  ls.sort()排序

#字典类型   dict ={ "key":value , : , ：}   dict[key]相当于自定义的序号  空字典  dict={}  dict.get(key)





#用来计算一组数据的平均值、方差、中位数

def getNum():  # 获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入一个数字: ")
    while iNumStr != "Q" and iNumStr != "q":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入一个数字(输入Q结束输入): ")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)


def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getNum()  # 主体函数
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n, m), median(n)))