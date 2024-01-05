import sys
N,M = map(int,sys.stdin.readline().split())

memo_list={}
for i in range(N):
    site,pw = (map(str,sys.stdin.readline().split()))
    memo_list[site]=pw
    
for j in range(M):
    site = (sys.stdin.readline().strip())
    print(memo_list[site])