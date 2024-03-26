import sys

input = sys.stdin.readline
n,q = map(int,input().split())
newcar = list(map(int,input().split()))
newcar.sort()
for _ in range(q):
    mid = int(input().strip())
    left,right = 0,n-1
    while left<= right:
        mid_idx = (left+right)//2
        if newcar[mid_idx]<mid:
            left = mid_idx+1
        elif newcar[mid_idx]> mid:
            right = mid_idx-1
        else:
            break
    else:
        print(0)
        continue
    print(mid_idx*(n-mid_idx-1))