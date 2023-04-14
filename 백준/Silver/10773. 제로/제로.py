import sys
from collections import deque
n = int(sys.stdin.readline())

list1=[]

def a(no):
    if no!=0:
        list1.append(no)
    else:
        list1.pop(-1)

    return list1

for i in range(n):
    no = int(sys.stdin.readline())
    a(no)
print(sum(list1))
