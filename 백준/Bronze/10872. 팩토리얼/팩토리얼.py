from sys import stdin as s
#s=open("input.txt","rt")

def fac(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fac(n-1)*n
    
n=int(s.readline())
print(fac(n))