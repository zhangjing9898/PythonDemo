#模拟文件类

class fileopen:
    #构造函数
    def __init__(self,filepath):
        self.file_object=open(filepath,"r+")

    #析构函数
        '''
    def __del__(self):
        print("delete the file object")
        self.file_object.close()
class Vector_point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector_point(x,y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
'''
#操作
#>>> p1=Vector_point(70,20)
#>>> p1
#<__main__.Vector_point instance at 0x03073D50>
#>>> p2=Vector_point(10,10)
#>>> (p1+p2).x
