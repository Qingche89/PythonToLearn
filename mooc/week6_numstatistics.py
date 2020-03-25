
#根据元组类型输入计算
def getNum():  # 获取用户不定长度的输入
    return eval(input())


def mean(numbers):  # 计算平均值
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    numbers = list(numbers)
    numbers.sort()
    lengh =len(numbers)
    if lengh%2 == 0:  #偶数
        return (numbers[int(lengh/2-1)] + numbers[int(lengh/2)])/2
    else:
        return numbers[int((lengh-1)/2)]

#n =tuple()
n = getNum()  # 主体函数
m = mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
