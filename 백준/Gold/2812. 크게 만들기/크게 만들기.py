import sys
from collections import deque

list1=[]
result_list=[]

#s=open("input.txt","rt")
stack =[]
n,k = map(int,sys.stdin.readline().split())
numbers=sys.stdin.readline().rstrip()


for num in numbers:
    while stack and k>0 and stack[-1]<num:
        stack.pop()
        k-=1
    stack.append(num)
if k>0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))