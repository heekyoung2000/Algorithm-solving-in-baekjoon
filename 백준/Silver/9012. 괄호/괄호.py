import sys
from collections import deque
#s=open('input.txt','rt')
n = int(sys.stdin.readline())


def a(no):
    cnt=0
    for i in range(len(no)):
        if no[i]=="(":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                break
                
    if cnt==0:
        print("YES")
    else:
        print("NO")
        

for i in range(n):
    no = list(map(str,sys.stdin.readline().strip()))
    a(no)
