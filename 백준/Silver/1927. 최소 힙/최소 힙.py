#최소힙

import sys
import heapq
#s=open("input.txt",'rt')
n=int(sys.stdin.readline())

hq=[]

def heap(number):
    if number==0:
        if len(hq)==0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq,number)

for i in range(n):
    number=int(sys.stdin.readline())
    heap(number)