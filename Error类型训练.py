'''
list1=range(100)
index=input("input the index:")
print(list1[index])
'''

list1=range(100)
while(1):
    try:
        index=input("input the index:")
        if(index%2==0):
            raise IndexError
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


