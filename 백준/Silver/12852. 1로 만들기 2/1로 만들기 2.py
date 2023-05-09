from sys import stdin as s

#s=open("input.txt","rt")
#dp로 풀기
n=int(s.readline())
dp=[i for i in range(n+1)] ## 누적 최소 횟수를 저장하는 배열
dp[1]=0

result=[i for i in range(n+1)]
result[1]=0

for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    result[i]=i-1
    
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i]=dp[i//3]+1
        result[i]=i//3
        
    if i%2==0 and dp[i]> dp[i//2]+1:
        dp[i]=dp[i//2]+1
        result[i]=i//2
    
target = n
print(dp[n])
print(n,end=" ")
while result[target] !=0:
    print(result[target],end=" ")
    target = result[target]