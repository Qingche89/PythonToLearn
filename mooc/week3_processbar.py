# -*- coding: utf-8 -*-


#M-3
#引入time随机标准库
import time as tm  #引入time随机标准库  标准库无需安装
print(tm.time())#1970年  时间戳
print(tm.ctime())
print(tm.strftime("%Y-%m-%d %H:%M:%S",tm.gmtime()))
starttime = tm.perf_counter()
tm.sleep(5)  #Do someting
print("耗时",starttime- tm.perf_counter())


#M-3
#文本进度条
import time
scale = 50
print("执行开始".center(scale, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]耗时:{:.2f}s".format(c,a,b,dur),end='')  # \r光标返回重新输入
    time.sleep(0.2)
print("\n"+"执行结束".center(scale,'-'))