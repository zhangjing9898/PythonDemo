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
        print("输入索引越界！")
    except NameError:
        print("你输入了个未定义的变量！")
    except TypeError as e:
        #print("您输入的不是一个整数！")
        print(e)
    except Exception as e:
        print(e)


