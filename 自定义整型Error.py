#����һ���ֵ�,keyֵ����Ϊ����������ͨ���Զ����쳣�׳�����ʾ������Ϊ������
#�������쳣������ͳһ�Ĵ�ӡ���������ʹ���

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
                raise keyTypeError("����������������");
    except keyTypeError as e:
        print(e)
    except:
        print("������")

#�ж�3Ϊ����  len(str(900))
