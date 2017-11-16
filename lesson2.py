"""
a=input("input a=")
b=input("input b=")

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

c=gcd(max(a,b),min(a,b))
print("result:",a*b/c)
"""

input_number=raw_input("input")
a=input_number.split(" ")
print(a)

i=0

while(i!=len(a)-1):
    if(a[i]==''):
        del a[i]
        i=i-1
    i=i+1

print(a)
