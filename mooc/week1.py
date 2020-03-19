#Mooc  Python基础语法框架  不涉及面向对象编程
#跟随嵩天老师团队学习  北京理工大学


#W-1:python基础语法元素

#Python温度转换实例
'''
      奋斗的人生不需要过多的解释
''' #多行注释
wendu  = str(input('输入温度：'))
#if wendu[-1] == 'F':  #正0/逆-1向序号  索引或者切片：   列表[] 或 元组()
if wendu[-1] in ['f' , 'F']:            # if in   和  while in
   #print("摄氏温度为",(int(wendu[0:-1])-32)/1.8,'C')
    c = (eval(wendu[0:-1])-32)/1.8       #eval评估函数  去最外侧引号并执行之
    print("华氏温度{:.2f}F摄氏温度为{:.2f}C".format(eval(wendu[0:-1]),c))     #格式化输出方法 写出带槽的模板字符串"{0:引导 .2精度 f%类型}{0:}{0:}{2:}".format(a,b,c)
elif wendu[-1] in ['C' , 'c']:      #elif<条件>：   elif
   print("华氏温度为",int(wendu[0:-1])*1.8+32,'F')
else:
  print("输入错误")