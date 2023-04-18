import sys
from heapq import heapify
import heapq
    
leftheap=[]
rightheap=[]
result=[]
n=int(sys.stdin.readline())
hq=[]
for i in range(n):
    num=int(sys.stdin.readline())
    
    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    if rightheap and leftheap[0][1]>rightheap[0][0]:
        min=heapq.heappop(rightheap)[0]
        max= heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap,(-min,min))
        heapq.heappush(rightheap,(max,max))
    
    result.append(leftheap[0][1])
    
for i in result:
    print(i)