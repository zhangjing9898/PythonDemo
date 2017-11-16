#输入一个字典,key值必须为整数，否则通过自定义异常抛出并提示“必须为整数”
#其他的异常，可以统一的打印，输入类型错误

class keyTypeError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

while(1):
    try:
        dic1=eval(raw_input("plz input the dic:"))
        for i in dic1.keys():
            if(isinstance(i,int)==False):
                raise keyTypeError("输入索引不是整数");
    except keyTypeError as e:
        print(e)
    except:
        print("出错了")

#判断3为整数  len(str(900))
