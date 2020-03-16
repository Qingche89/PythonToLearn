# -*- coding: utf-8 -*-


#计算BMI值

def bmi(height,weight):
    return weight / pow(height, 2)

height, weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]: "))
bmi =bmi(height,weight)
print("BMI 数值为：{:.2f}".format(bmi))
nat = ""
if bmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= bmi < 24:
    nat = "正常"
elif 24 <= bmi < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为:国内'{0}'".format(nat))

#请输入身高(米)和体重\(公斤)[逗号隔开]: 1.9 ,  95
#BMI 数值为：26.32
#BMI 指标为:国内'偏胖'
    
#height = 1.9
#i = 95
##bmi =bmi(height,i)    #把一个变量用了函数名来命名，结果再调这个函数的时候就会报这个异常
#
#while bmi(height,i)> 22:
#    i -=0.1
#print("标准体重为{0:.2f}kg,需要减肥{1:.2f}斤,此时BMI指标为{2:.2f}".format(i,(95-i)*2,bmi(height,i)))
##标准体重为79.40kg,需要减肥31.20斤,此时BMI指标为21.99

    