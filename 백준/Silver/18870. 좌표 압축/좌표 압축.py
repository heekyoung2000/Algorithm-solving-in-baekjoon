from sys import stdin as s
#s=open("input.txt","rt")
n=int(s.readline())
num_list=list(map(int,s.readline().split()))
set_list=sorted(set(num_list))

dic = {set_list[i]:i for i in range(len(set_list))}
for i in num_list:
    print(dic[i],end=" ")