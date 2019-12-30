# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:18:31 2019

@author: Xin
"""
import jieba
import wordcloud


# 读取 新时代中国特色社会主义
f = open("新时代中国特色社会主义.txt", "r", encoding = "utf-8")
t = f.read()
f.close()

# 将文本进行分词
ls = jieba.lcut(t)
txt = " ".join(ls)

# 生成词云对象
w = wordcloud.WordCloud(font_path="simkai.ttf", width = 1000, height = 800,
                        background_color="white", max_words=15)
w.generate(txt)
w.to_file("grwordcloud.png")


