#1.不使用reverse函数,实现一个整数列表的反序
'''
a = eval(raw_input("Input a list:"))
i  = 0
j = len(a)-1
while(i<j):
    a[i],a[j] = a[j],a[i]
    i+=1
    j-=1
print a
'''

#2.生成并打印一个长度为100的考洛尔列表

num = cnt = 1
List = []
a = [0,1]
while(len(List)<10):
    for i in range(a[-1]):
        b = []
        for j in range(cnt):
            b.append(num)
            num += 1
        List.append(b)
    cnt += 1
    a.append(a[-1])
print List





    


