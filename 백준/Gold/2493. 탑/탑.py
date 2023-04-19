import sys
from collections import deque

#s=open("input.txt",'rt')
n=int(sys.stdin.readline())
dq=deque()

def stack(list1):
    result=[0]*n
    for i in range(len(list1)):
        while dq:
            if list1[dq[-1]]<list1[i]:
                dq.pop()
            else:
                result[i]=dq[-1]+1
                break
        dq.append(i)
    return result  


list1=list(map(int,sys.stdin.readline().split()))
for i in stack(list1):
    print(i,end=" ")