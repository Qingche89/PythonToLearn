#逆置cvs

f = open("D:/Code/PythonToLearn/data/data.csv","r")
line  = f.readlines()
line = line[::-1]  #利用切片步长-1完成倒序

for x in line:
    x=x.replace(" ",'')
    x=x.strip("\n")
    x=x.replace(",",";")
    x= x[::-1]    #利用切片步长-1完成倒序
    print(x)