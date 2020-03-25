#将输入的字典转化

s = input("输入字典：")
try:
    d = eval(s)
    e = {}
    for key in d:
        e[d[key]] = key
    print(e)
except:
    print("输入错误")

#input:   {"a": 1, "b": 2}