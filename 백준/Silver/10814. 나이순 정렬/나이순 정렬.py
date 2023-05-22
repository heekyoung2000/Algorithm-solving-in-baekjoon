from sys import stdin as s
from collections import deque
#s=open("input.txt","rt")
#python은 stable 정렬- 입력받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지

n=int(s.readline())
list1=[]
for _ in range(n):
    num,name = map(str,s.readline().split())
    num=int(num)
    list1.append((num,name))
    
list1.sort(key=lambda x : x[0])

for i in list1:
    print(i[0], i[1])