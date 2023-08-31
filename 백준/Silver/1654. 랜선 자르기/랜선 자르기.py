from sys import stdin as s

N,K = map(int,s.readline().split())
arr=[]
for i in range(N):
    arr.append(int(s.readline()))
    
start = 1
end = max(arr)

while (start <=end):
    mid=(start+end)//2
    cnt=0
    for i in arr:
        cnt+= i//mid
    if cnt >= K:
        start = mid+1
    else:
        end = mid -1
print(end)