import sys
#남학생(1)이 받은 스위치 번호가 자기가 받은 수의 배수- 스위치 상태 바꾸기
#여학생(2)이 받은 스위치 번호를 중심으로 좌우 대칭 - 스위치 좌우 대칭인 부분+받은 번호 바꾸기

s_num = int(sys.stdin.readline().strip())
s_status = list(map(int,sys.stdin.readline().split()))

stu_num = int(sys.stdin.readline().strip())
#1 2 3 4 5 6 7 8
#0 1 0 1 0 0 0 1
#남-3,6스위치 바꿈
#0 1 1 1 0 1 0 1
#여-3 기준으로 좌우대칭이면 스위치 바꿈
#1 0 0 0 1 1 0 1

for i in range(stu_num):
    sex,get = map(int,sys.stdin.readline().split())
    #남자 일경우 계산
    if sex==1:
        get_mul=1
        multiple=get
        while multiple<=s_num:
            if s_status[multiple-1]==0:
                s_status[multiple-1]=1
                
            else:
                s_status[multiple-1]=0
            get_mul+=1
            multiple=get_mul*get
                
    #여자 일경우 계산
    else:
        mul=0
        get-=1
        while get+mul<s_num and get-mul>=0 and s_status[get+mul]==s_status[get-mul]:
            if s_status[get+mul]==1:
                s_status[get+mul],s_status[get-mul]=0,0
            else:
                s_status[get+mul],s_status[get-mul]=1,1
            mul+=1
            
        
            
for s in range(0,s_num):
    if s==20 or s==40 or s==60 or s==80:
        print()
        print(s_status[s],end=" ")
    else:
        print(s_status[s],end=" ")