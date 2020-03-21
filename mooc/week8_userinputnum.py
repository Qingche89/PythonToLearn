try:
    s = eval(input("请输入任意数字或数学计算式:"))
except :                    #Exception过于宽泛
    print("输入有误")
print("平方的结果为：",s**2)