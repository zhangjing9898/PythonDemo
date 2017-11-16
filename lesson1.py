a=input("input a=")
b=input("input b=")
max_factor=1
for i in range(min(a,b),2,-1):
    if((a%i==0) and (b%i==0)):
        max_factor=i

print(max_factor)
        
