import re
import urllib
import os

#��ȡhttpԶ���ļ�
root="http://www.nsu.edu.cn"
path="http://www.nsu.edu.cn/HTML/image/article_60.html"

page=urllib.urlopen(path)
content=page.read()

#����������ʽ
reg=r'href="(.+?\.jpg)"'
pattern=re.compile(reg)
list1=pattern.findall(content)
count=0

for i in list1:
    path=root+i
    
    count=count+1
    if(os.path.exists("D:\\����")==False):
        os.mkdir("D:\\����")
    if(count==1):
        continue
    else:
        urllib.urlretrieve(path,"D:/����/"+str(count)+".jpg")

print("�ɹ���ȡ"+str(count)+"��ͼƬ")

