import os
import re
file1=open("C:\Users\ZJ\Desktop\ѧ������.txt")
a=file1.readlines()
#����2��������ʽ��pattern����һ������ƥ��ѧ�ţ���һ������ƥ��ѧ�Ÿ�ʽ
pattern1=re.compile(r'\d+');
pattern2=re.compile(r'1[0-9]{10}');
#(pattern2.match(pattern1.findall(k)[0])==None)or
for i,k in enumerate(a):
    if (pattern2.match(pattern1.findall(k)[0])==None)or(pattern2.match(pattern1.findall(k)[0]).group()!=pattern1.findall(k)[0]):
        print("ѧ�Ŵ���"+pattern1.findall(k)[0] +":"+k.replace(pattern1.findall(k)[0],'').strip())
file1.close();
