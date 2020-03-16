# -*- coding: utf-8 -*-
#凯撒密码
#print(chr(ord('a')+3))
#ord(Unicode字符)返回ASCII码  chr()反之

s = input("输入原文：")
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
        print(ord('a') + ((ord(c)-ord('a')) + 3 )%26)
    elif 'A' <= c <= 'Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
        print(ord('A') + ((ord(c)-ord('A')) + 3 )%26)
    else:
        t += c
print("密码输出{0:}".format(t))