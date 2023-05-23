from sys import stdin as s
#s=open("input.txt","rt")
n,m = map(int,s.readline().split())
array=[]
result=[]
for _ in range(n):
    num=int(s.readline().strip())
    array.append(num)
array.sort()
## 투포인터 사용
i=0
j=0
while i<len(array) and j<len(array):
    dif = abs(array[i]-array[j])
    if m <=dif:
        result.append(dif)
        i+=1
    if m>dif:
        j+=1
print(min(result))