'''
try:
    a=0
    a=a+1
    a=a/0
except NameError:
    print("����aû�ж��壡");
except ZeroDivisionError:
    print("0������������");
'''
try:
    a=0
    a=a+1
    raise NameError
    a=a
except (NameError,ZeroDivisionError):
    print("�����ˣ�");

#raise �׳��쳣

    
