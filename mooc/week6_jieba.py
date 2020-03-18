

#jieba第三方库  中文分词
#pip install jieba

import jieba as jb
jb.add_word("宋一楠")
print(jb.lcut("宋一楠是个好人正直的人"))