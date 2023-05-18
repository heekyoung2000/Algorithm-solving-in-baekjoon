from sys import stdin as s

#s=open("input.txt","rt")
m=123456
array1 = [i for i in range(2*m+1)]
new_array=[]

def is_prime(a):
    for i in range(2,int(a**(1/2))+1):
        if a%i==0:
            return False
    return True
    
for i in array1:
    if is_prime(i):
        new_array.append(i)

while 1:
    num=0
    n=int(s.readline())
    if n==0:
        break
    elif n==1:
        num=1
    else:
        for i in new_array:
            if n<i <= 2*n:
                num+=1
    print(num)