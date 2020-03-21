#数组的妙用  进行大小写的转换
template = "零一二三四五六七八九"  #大写的汉字模板  利用list/数组巧妙对应
s = input("输入数字：")
try:
    for i in s:
        print(template[eval(i)], end="")
except:
    print("输入异常!")