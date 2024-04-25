import sys
from itertools import product
input =sys.stdin.readline

N,K = map(int,input().split())
k_list = list(map(str,input().split()))

k_list=sorted(k_list,reverse=True)
leng = len(str(N))

s = ""
while True:
    cand = list(product(k_list,repeat=leng))
    ret =[]
    for i in cand:
        temp = int("".join(map(str,i)))
        if temp <=N:
            ret.append(temp)
    
    if len(ret) >=1:
        print(max(ret))
        break
    else:
        leng-=1
        