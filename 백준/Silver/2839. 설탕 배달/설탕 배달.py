N=int(input())
m=N//3

result=5000
for i in range(m+1):
    num = N-3*(m-i)
    if num%5==0:
        result= min((m-i+(num//5)),result)
    
if result==5000:
    print(-1)
else:
    print(result)