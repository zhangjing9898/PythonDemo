##a=[23,45,67,100,203]
##
##for i in range(5):
##    print("index is "+str(i)+" and the value is "+str(a[i]));
##else:
##    print("±éÀú½áÊø");

    
a=eval(raw_input("a="))

for i,j in enumerate(a):
    if(type(j)!=int):
        del a[i]
print(a)
