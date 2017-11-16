'''
a=[i*i*i for i in range(1,26)]
#这是1到20000之间的立方数
'''

'''
第二种，使用字典推导：
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m
{'d': 4, 'a': 1, 'b': 2, 'c': 3}
>>> {v: k for k, v in m.items()}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
'''

'''
import os
import re
file1=open("d:\\学生名单.txt")
a=file1.readlines()
pattern1=re.compile(r'\d+')
for i,k in enumerate(a):
    a[i]=k.replace(pattern1.match(k).group(),'').strip()+pattern1.match(k).group()
for i in a:
    os.makedirs("d:\\考试成绩new\\"+i);
'''

'''
import os
import re
file1=open("d:\\学生名单.txt")
a=file1.readlines()
pattern1=re.compile(r'\d+')
for i,k in enumerate(a):
    a[i]=k.replace(pattern1.match(k).group(),'').strip()+pattern1.match(k).group()
#for i in a:
#    os.makedirs("d:\\考试成绩new\\"+i);
print(a);
file1=open("d:\\学生名单.txt",'w');
file1.writelines(a);
file1.close();
'''
#pattern1.findall("12321321 wrr 15310920101eee")
#上面这个是查询
