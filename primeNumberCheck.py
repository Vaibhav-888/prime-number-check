from math import *

def is_prime(n):
    
    if n <= 1:
        return False
        
    for i in range(2, int(sqrt(n)) + 1):
        if n % 2 == 0:
            return False
        elif n == i:
            return True
            
    return True
        
print(is_prime(5))