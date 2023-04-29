n,k=map(int,input().split())
count =0
list1=[]

for i in range(0,n):
    s=int(input())
    list1.append(s)
list1.reverse()

for j in range(len(list1)):
    if k<list1[j]:
        j+=1
    else:
        count+=k//list1[j]
        k%=list1[j]

print(count)