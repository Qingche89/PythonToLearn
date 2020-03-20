
# 生成工作会议的词云
import jieba
import wordcloud
f = open("D:/MyCode/PythonToLearn/data/中心第一次工作会议.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)

w = wordcloud.WordCloud( \
    width = 1000, height = 700, \
    background_color = "white", \
    stopwords={"中心" ,"继续" ,"做好" ,"各项" ,"工作" ,"增加" ,"有关" ,"推进"},  # 设置停用词
    font_path = "msyh.ttf"  , \
    max_words = 20
)
w.generate(txt)
w.to_file("D:/MyCode/PythonToLearn/creat/grwordcloud.png")
print("图片已生成")

# "做好","有关","确保","牵头","要求","继续","各项","工作","到位"
