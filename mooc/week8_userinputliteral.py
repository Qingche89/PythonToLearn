# 过滤英文单词   放开输入 鲁棒性
s = input("请输入任意字符串:")
out_str =''
for c in s:
    if (c>='a' and c<='z') or (c>='A' and c<='Z' ):
        out_str += c
print('过滤的结果为：',out_str)


'''
alpha = [] #生成字母表alpha
for i in range(26):
    alpha.append(chr(ord('a') + i))
    alpha.append(chr(ord('A') + i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")
'''
