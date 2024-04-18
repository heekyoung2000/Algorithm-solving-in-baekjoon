from collections import deque
n=int(input())
count=0
list1=[0,1]
i=1
while len(list1)!=n+1:
    s=list1[i-1]+list1[i]
    list1.append(s)
    i+=1

print(list1[n])