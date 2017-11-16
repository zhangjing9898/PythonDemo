#通过继承基类exception 自定义一个异常类
class keyTypeException(Exception):
    def __init__(self,msg):  #魔法方法
        self.msg=msg
    def __str__(self):
        return self.msg

list1=range(100)
while(1):
    try:
        index=eval(raw_input("input the index:"))
        if(index%2==0):
            raise keyTypeException("输入的索引不允许为偶数")  #主动抛出异常
        value=list1[index]
        print("list"+str(index)+"="+str(value))
    except IndexError:
        print("输入索引越界！")
    except NameError:
        print("你输入了个未定义的变量！")
    except TypeError as e:
        #print("您输入的不是一个整数！")
        print(e)
    except Exception as e:
        print(e)
