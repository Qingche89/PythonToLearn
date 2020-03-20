

#W-7：文件和数据的格式化


#读取数据脚本及数据接口的定义
#exp  300,0,144,1,0,0
#  行进距离 转向判断 0：左转 1：右转  转向角度  RGB三个通道颜色（0-1之间的浮点数）

import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("D:/Code/PythonToLearn/data/drawdata.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.rt(datals[i][2])
    else:
        t.lt(datals[i][2])