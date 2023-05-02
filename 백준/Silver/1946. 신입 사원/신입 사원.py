from sys import stdin as s
from collections import deque
T=int(s.readline()) # 테스트 케이스 수

def count_peo(test_list):
    main_rank=test_list[0][1]
    count=1
    k=1
    for i in range(k,N):
        if main_rank>test_list[i][1]:
            count+=1
            main_rank=test_list[i][1]
            k=i+1
    print(count)
        
    

for _ in range(T):
    N=int(s.readline()) # 지원자의 숫자
    visited =[0]*(N+1)
    test_list=[]
    for _ in range(N):
        score_test, score_face = map(int,s.readline().split())
        test_list.append((score_test,score_face))
    test_list.sort()
    count_peo(test_list)
  
    