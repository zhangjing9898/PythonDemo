#ͨ���̳л���exception �Զ���һ���쳣��
class keyTypeException(Exception):
    def __init__(self,msg):  #ħ������
        self.msg=msg
    def __str__(self):
        return self.msg

list1=range(100)
while(1):
    try:
        index=eval(raw_input("input the index:"))
        if(index%2==0):
            raise keyTypeException("���������������Ϊż��")  #�����׳��쳣
        value=list1[index]
        print("list"+str(index)+"="+str(value))
    except IndexError:
        print("��������Խ�磡")
    except NameError:
        print("�������˸�δ����ı�����")
    except TypeError as e:
        #print("������Ĳ���һ��������")
        print(e)
    except Exception as e:
        print(e)
