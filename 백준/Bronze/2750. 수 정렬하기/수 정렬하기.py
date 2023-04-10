def insertion_sort(list1):
    for i in range(1,n):
        j=i
        tmp=list1[i]
        while j>0 and list1[j-1]>tmp:
            list1[j]=list1[j-1] # 큰값을 뒤에 저장
            j-=1
        list1[j]=tmp #작은 값을 앞에 저장

n=int(input())
list1=[]
for i in range(n):
    number=int(input())
    list1.append(number)

insertion_sort(list1)
for j in list1:
    print(j)
