# -*- coding: utf-8 -*-

#复利计算
corpus = 1.0
profit_rate = 0.001
loss_rate = 0.001
for i in range(365):
   if i % 7 in [6,0]:
       corpus = corpus*(1-loss_rate)
   else:
       corpus = corpus*(1+profit_rate)
print("工作日的力量：{:.2f} ".format(corpus))

