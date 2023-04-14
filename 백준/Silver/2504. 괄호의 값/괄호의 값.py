import sys
from collections import deque

dq=deque()

def result(n):
    res=0
    temp=1
    for i in range(len(n)):
        if n[i]=='(':
            dq.append(n[i])
            temp*=2
        elif n[i]=='[':
            dq.append(n[i])
            temp*=3
        elif n[i]==']':
            if n[i-1]=='[':
                res+=temp
                
            if not dq or dq[-1]=='(':
                res=0
                break
            
            temp=temp//3
            dq.pop()
    
        elif n[i]==')':
            if n[i-1]=='(':
                res+=temp
                
            if not dq or dq[-1]=='[':
                res=0
                break
            
            temp=temp//2
            dq.pop()
    
    if len(dq)!=0:
        res=0
                
    print(res)        
             

#s=open('input.txt','rt')
n =list(map(str,sys.stdin.readline().strip()))
result(n)



