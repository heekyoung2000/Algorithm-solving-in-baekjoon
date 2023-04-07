a=int(input())
b=int(input())
c=int(input())
result = a*b*c
list1 = list(map(int, str(result)))

for i in range(10):
    print(list1.count(i),end="\n")