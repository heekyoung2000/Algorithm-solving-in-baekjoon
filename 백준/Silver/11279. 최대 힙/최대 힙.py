import sys
import heapq


#s=open("input.txt",'rt')
n=int(sys.stdin.readline())

hq = []

def heap(a):
    if a==0:
        if len(hq)==0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])#마이너스를 붙임으로써 큰 숫자부터 출력
    elif a!=0:
        heapq.heappush(hq,(-a,a))
        
    return

for i in range(n):
    number = int(sys.stdin.readline())
    heap(number)