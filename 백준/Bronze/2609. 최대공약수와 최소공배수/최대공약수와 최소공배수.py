import sys
a,b=map(int,sys.stdin.readline().split())
result1=[]

if a>b:
    len=a
else:
    len=b
for i in range(1,len+1):
  if a%i==0 and b%i==0:
    result1.append(i)

m=max(result1)
print(m)
print((a//m)*(b//m)*m)