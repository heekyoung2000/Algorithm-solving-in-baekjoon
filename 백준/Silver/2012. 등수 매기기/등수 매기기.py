from sys import stdin as s
#s=open("input.txt","rt")

n=int(s.readline())
list1=[]
for _ in range(n):
    grade = int(s.readline())
    list1.append(grade)

list1.sort()
sum=0
for i in range(n):
    if i+1 == list1[i]:
        continue
    else:
        sum+=abs((i+1)-list1[i])
print(sum)