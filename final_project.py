#encoding:utf-8
"""
程序：基于Python和Gelphi的《黎明破晓的街道》人物关系图谱构建
作者：谭薇
"""
import os,sys
import jieba,codecs,math
import jieba.posseg as pseg
names={}  #姓名字典
relationships={} #关系字典
lineNames=[]  #每段人物关系
#设置字典,加载
jieba.load_userdict('dict.txt')
with codecs.open("黎明破晓的街道.txt",'r','gbk') as f:
    for line in f.readlines():
        poss=pseg.cut(line)  #分割并返回该词词性
        lineNames.append([])#为新读入的一段添加人物名称列表
        for w in poss:   
            if  w.flag!="nr" or len(w.word) <2:
                continue #当分词长度小于2或该词词性不为nr时认为该词不为人名
            lineNames[-1].append(w.word) #为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1#该人物出现次数加 1
    for name,times in names.items():
        print (name,times)
#根据识别结果构架网络
for line in lineNames:  #对于每一段
   for name1 in line:
      for name2 in line: #每一段中两个任意人
          if name1==name2:
              continue
          if relationships[name1].get(name2) is None:
            relationships[name1][name2]=1
          else:
            relationships[name1][name2]+=1#两个人的名字一同出现
#过滤冗余的边并输出结果，将已经建立好的names和relationships输出到文本，，输出
#节点集合保存在 "黎明破晓的街道_node.csv"

with codecs.open('黎明破晓的街道_node.csv','w','gbk') as f:
    f.write("id lable weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")
#边集合保存在 "黎明破晓的街道_edge.csv"
with codecs.open('黎明破晓的街道_edge.csv','w','gbk') as f:
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>1:
                f.write(name+ " "+v+" "+str(w)+"\r\n")
