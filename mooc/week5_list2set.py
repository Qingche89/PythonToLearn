

#利用list转set去重

n = str(input("输入一串数字："))
list = []
for c in n:
    list.append(c)
cl = set(list)    #利用list转set去重
sum=0
for d in cl:
    sum+=int(d)
print("去重求和的结果为：",sum)