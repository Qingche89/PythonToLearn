

#哈姆雷特的词频统计


def getText():
    txt = open("D:/Code/PythonToLearn/data/hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


hamletTxt = getText()
words = hamletTxt.split()
counts = {}#利用字典类型映射对应完成统计
for word in words:
    counts[word] = counts.get(word, 0) + 1
    #get(key[, default])  如果 key 存在于下层映射中则返回 key 的值，否则返回 default
    #{key/word : value/counts,}
items = list(counts.items())  #返回元组列表视图 由dict.keys(), dict.values() 和dict.items() 所返回的对象是 视图对象
#  [(word,counts), ]
items.sort(key=lambda x: x[1], reverse=True)  #排序sort(*, key=None, reverse=False)  #将一个列表按照键值对的两个元素的第二个元素进行排序
for i in range(10):
    word, count = items[i]  #视图  返回的是元组  word, count = items[i][0],items[i][1]
    print("{0:<10}{1:>5}".format(word, count))