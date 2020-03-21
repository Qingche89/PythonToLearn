#计算每行字数


file = open("D:/Code/PythonToLearn/data/latex.log","r")
zishu = 0
hangshu = 0
for line in file:
    reall = line.strip("\n")
    if  reall != "":
       hangshu+=1
       zishu += len(reall)

print(round(zishu/hangshu))
file.close()