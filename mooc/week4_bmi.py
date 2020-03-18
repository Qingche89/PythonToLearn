# -*- coding: utf-8 -*-


# 计算BMI值
def bmi(height, weight):
    return weight / pow(height, 2)



height, weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]: "))
mybmi = bmi(height, weight)
'''
bmi =bmi(height,weight)    #把一个变量用了函数名来命名，结果再调这个函数的时候就会报这个异常
TypeError: 'float' object is not callable  #调用时报错，此时bmi已经指向了一个浮点数
'''

print("BMI 数值为：{:.2f}".format(mybmi))
nat = ""
if mybmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= mybmi < 24:
    nat = "正常"
elif 24 <= mybmi < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为:国内'{0}'".format(nat))

standard_weight = weight - 0.1
#如何减肥
while bmi(height,standard_weight)> 22: #22打好稳定基础
   standard_weight -=0.1
print("标准体重为{0:.2f}kg,需要减肥{1:.2f}斤,此时BMI指标为{2:.2f}".format(standard_weight,(weight-standard_weight)*2,bmi(height,standard_weight)))



# 请输入身高(米)和体重\(公斤)[逗号隔开]: 1.9 ,  95
# BMI 数值为：26.32
# BMI 指标为:国内'偏胖'
#标准体重为79.40kg,需要减肥31.20斤,此时BMI指标为21.99

