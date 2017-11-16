import os
import re
file1=open("C:\Users\ZJ\Desktop\学生名单.txt")
a=file1.readlines()
#创建2个正则表达式的pattern对象，一个用来匹配学号，另一个用来匹配学号格式
pattern1=re.compile(r'\d+');
pattern2=re.compile(r'1[0-9]{10}');
#(pattern2.match(pattern1.findall(k)[0])==None)or
for i,k in enumerate(a):
    if (pattern2.match(pattern1.findall(k)[0])==None)or(pattern2.match(pattern1.findall(k)[0]).group()!=pattern1.findall(k)[0]):
        print("学号错误"+pattern1.findall(k)[0] +":"+k.replace(pattern1.findall(k)[0],'').strip())
file1.close();
