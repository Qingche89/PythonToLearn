

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
    #get(key[, default])   Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None
    #{key/word : value/counts,}
items = list(counts.items())             #Return a new view of the dictionary’s items ((key, value) pairs)
#  [(word,counts), ]
items.sort(key=lambda x: x[1], reverse=True)  #sort(*, key=None, reverse=False)  #将一个列表按照键值对的两个元素的第二个元素进行排序
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))