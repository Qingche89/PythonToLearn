# -*- coding: utf-8 -*-

#复利率计算
#工作日增益0.001  一月休息两日损失0.001
corpus = 1.0
profit_rate = 0.001
loss_rate = 0.001
for i in range(365):
   if i % 30 in [0,16]:
       corpus = corpus*(1-loss_rate)
   else:
       corpus = corpus*(1+profit_rate)
print("工作日的力量：{:.2f} ".format(corpus))