from math import sqrt  
def is_prime(n):  
    if n == 1:  
        return False  
    for i in range(2, int(sqrt(n))+1):  
        if n % i == 0:  
            return False  
    return True  
  
count = 0  
for i in range(1, 1000):  
    if is_prime(i):  
        count = count + 1  
        print(i)
