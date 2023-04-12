import math
import sys
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


T=int(sys.stdin.readline())
list1=[]
for i in range(T):
    n=int(sys.stdin.readline())
    list1.append(n)
for j in list1:
    result=[]
    for i in range(2,j//2+1):
        if is_prime(i) is True and is_prime(j-i) is True:
            result.append(i)
    m=max(result)
    print(f'{m} {j-m}')