from sys import stdin as s

#s=open("input.txt","rt")
n=int(s.readline())
array_list = list(map(int,s.readline().split()))
dp=[1]*n



for i in range(0,n):
    for j in range(0,i):
        if array_list[i]>array_list[j]:
            dp[i]=max(dp[i],dp[j]+1)
            
print(max(dp))
result=[]
max_result=max(dp)
for i in range(n-1,-1,-1):
    if dp[i]==max_result:
        result.append(array_list[i])
        max_result-=1
result.reverse()        
print(*result)
            