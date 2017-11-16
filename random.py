#随机产生26个字母
import math
import random

def create_char_list():
    a=[]
    for i in range(1,27):
        a.append(chr(i+96))
    return a


#从列表中返回一个随机字母
def get_random_char(a):
    return a[int(random.random()*len(a))]

#创建字典
dic1={}
list1=create_char_list()
for i in range(1,27):
    dic1[i]=list1.pop(list1.index(get_random_char(list1)))
    
print(dic1);



    
