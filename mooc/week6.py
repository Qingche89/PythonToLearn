#M-6
#组合数据类型  包括 集合类型  序列类型：字符串"" 列表[] 元组()    字典/映射类型

#集合类型：无序的不同元素{，，}
#运算操作符 并|  差- 交& 补^     关系比较 子集<  包含>
#方法  S.add()  remove()  clear()清空  pop()随机取走 copy()副本 len() set()转集合/初始化/可表示空
#应用集合数据去重
ls = [1,3,4,5,12,2,3,53,3,1,2]
A= set(ls)
ls = list(A)
print(ls)

#序列类型：一组有序的元素  字符串""   列表[] 元组()  序号为正向0/逆向-1  操作符  索引和切片  复制*n  连接+
#方法  len()  min() max() index() count()
#字符串"" 略
#元组()  创建初始化(，，)或，，或tuple()  多用于函数多值返回return为元组（），（）可以省略  不能被修改
#列表[]  创建初始化[]或list()  ls[i]替换 del ls[i]删除  ls.append(x)追加  ls.reverse()反转  ls.sort()排序

#字典类型   dict ={ "key":value , : , ：}   dict[key]相当于自定义的序号  空字典  dict={}  dict.get(key)


#M-6
#jieba第三方库  中文分词
#pip install jieba

import jieba as jb
jb.add_word("宋一楠")
print(jb.lcut("宋一楠是个好人正直的人"))