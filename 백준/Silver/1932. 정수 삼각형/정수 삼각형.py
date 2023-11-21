n = int(input())
x=[0]*n
for w in range(n):
    x[w] = list(map(int,input().split()))

for i in range(1,n):
    for j in range(len(x[i])):
        if j==0:
            x[i][j]+=x[i-1][j]
        elif j== len(x[i])-1:
            x[i][j]+= x[i-1][j-1]
        elif j < len(x[i-1]):
            x[i][j] += max(x[i-1][j], x[i-1][j-1])
        
print(max(x[n-1]))
    