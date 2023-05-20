from sys import stdin as s
#s=open("input.txt","rt") #버블 정렬 문제
num_list=list(s.readline().split())
while sorted(num_list)!=num_list:
    for i in range(1,len(num_list)):
        if num_list[i-1]>num_list[i]:
            num_list[i-1],num_list[i]=num_list[i],num_list[i-1]
            print(" ".join(num_list))