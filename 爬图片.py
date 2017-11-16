import re
import urllib
import os

#读取http远程文件
root="http://www.nsu.edu.cn"
path="http://www.nsu.edu.cn/HTML/image/article_60.html"

page=urllib.urlopen(path)
content=page.read()

#构造正则表达式
reg=r'href="(.+?\.jpg)"'
pattern=re.compile(reg)
list1=pattern.findall(content)
count=0

for i in list1:
    path=root+i
    
    count=count+1
    if(os.path.exists("D:\\爬虫")==False):
        os.mkdir("D:\\爬虫")
    if(count==1):
        continue
    else:
        urllib.urlretrieve(path,"D:/爬虫/"+str(count)+".jpg")

print("成功爬取"+str(count)+"张图片")

