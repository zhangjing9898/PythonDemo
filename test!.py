#coding=utf-8
import random
dic={}
for i in range(26):
    dic[chr(i+65)]=0
for i in range(200):
    num=random.randint(65,90)
    dic[chr(num)]+=1
cha='a'
cnt=0
for i in range(26):
    if cnt<dic[chr(65+i)]:
        cnt=dic[chr(65+i)]
        cha=chr(65+i)
print("字母%c的输出频率最高为%d次"%(cha,dic[cha]))
