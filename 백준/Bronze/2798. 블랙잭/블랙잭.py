from sys import stdin as s
from itertools import combinations,permutations

n,m = map(int,s.readline().split())
list1 = list(map(int,s.readline().split()))
combi = list(combinations(list1,3))
list2=[]
result=0
for i in sorted(combi):
    s = sum(i)
    if s==m:
        result=s
    elif s<m:
        list2.append(s)
        
if result==0:
    print(max(list2))
else:
    print(result)
    