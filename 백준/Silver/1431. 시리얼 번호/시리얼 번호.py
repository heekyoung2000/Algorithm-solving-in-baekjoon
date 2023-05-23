from sys import stdin as s

#s=open("input.txt","rt")
#num_list=['0','1','2','3','4','5','6','7','8','9']
N= int(s.readline())
siral_list=[]
for _ in range(N):
    count=0
    siral = s.readline().strip()
    for i in siral:
        if i.isdigit():
            count+=int(i)
    num=len(siral)
    siral_list.append((num,siral,count))
#1. 비교하는 시리얼 번호 a,b가 길이가 다를때, 짧은 것이 먼저옴
siral_list.sort(key=lambda x : (x[0],x[2],x))# 숫자인것만 더했을 때 더 작은 값을 먼저 놓는다.
for i in range(len(siral_list)):
     print(siral_list[i][1])