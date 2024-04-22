import sys
from collections import deque

input =sys.stdin.readline

n=int(input())
num_list=deque()
num_list.append(0)
num_list.append(1)
i=1
if n==0:
    print(0)
else:
    while n!=i:
        fibo = num_list[0]+num_list[1]
        num_list.append(fibo)
        num_list.popleft()
        i+=1
    print(num_list[-1])