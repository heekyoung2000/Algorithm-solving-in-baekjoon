n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)

list1.sort()
for j in list1:
    print(j)