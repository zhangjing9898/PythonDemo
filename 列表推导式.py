'''
a=[i*i*i for i in range(1,26)]
#����1��20000֮���������
'''

'''
�ڶ��֣�ʹ���ֵ��Ƶ���
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m
{'d': 4, 'a': 1, 'b': 2, 'c': 3}
>>> {v: k for k, v in m.items()}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
'''

'''
import os
import re
file1=open("d:\\ѧ������.txt")
a=file1.readlines()
pattern1=re.compile(r'\d+')
for i,k in enumerate(a):
    a[i]=k.replace(pattern1.match(k).group(),'').strip()+pattern1.match(k).group()
for i in a:
    os.makedirs("d:\\���Գɼ�new\\"+i);
'''

'''
import os
import re
file1=open("d:\\ѧ������.txt")
a=file1.readlines()
pattern1=re.compile(r'\d+')
for i,k in enumerate(a):
    a[i]=k.replace(pattern1.match(k).group(),'').strip()+pattern1.match(k).group()
#for i in a:
#    os.makedirs("d:\\���Գɼ�new\\"+i);
print(a);
file1=open("d:\\ѧ������.txt",'w');
file1.writelines(a);
file1.close();
'''
#pattern1.findall("12321321 wrr 15310920101eee")
#��������ǲ�ѯ
