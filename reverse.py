'''
a=range(101)

b=[]

def reverse_list(list1):
    for i in range(-1,-102,-1):
        b.append(a[i])
    return b

print(reverse_list(a));
'''
'''
a=range(101)

b=[]

def reverse_list(list1):
    for i in range((int)(len(a)/2)):
        a[i],a[-i-1]=a[-i-1],a[i]

reverse_list(a);
print(a);
'''
'''
a=eval(raw_input(""))
b=[]

def solve(m):
    for i in m:
        if(type(i)!=list):
            b.append(i)
        else :
            solve(i)

solve(a)
print(b)
'''



