'''
try:
    a=0
    a=a+1
    a=a/0
except NameError:
    print("变量a没有定义！");
except ZeroDivisionError:
    print("0不能做除数！");
'''
try:
    a=0
    a=a+1
    raise NameError
    a=a
except (NameError,ZeroDivisionError):
    print("出错了！");

#raise 抛出异常

    
