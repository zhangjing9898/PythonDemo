import os
def count(ans,root):
    a=os.listdir(root)
    for i in range(len(a)):
        b=root+"/"+a[i]
        if(os.path.isfile(b)):
            ans+=1
        else:
            ans+=count(0,b)
    return ans
root="C:/Windows"
print(count(0,root))

        
