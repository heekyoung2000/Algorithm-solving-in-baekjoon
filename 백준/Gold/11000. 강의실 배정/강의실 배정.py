from sys import stdin
import heapq
input = stdin.readline


N = int(input())
class_list = []
for i in range(N):
    start,end = map(int,input().split())
    class_list.append([start,end])
s_list=sorted(class_list)
result=[]
heapq.heappush(result,s_list[0][1]) #첫 강의의 끝나는 시간 넣기
for i in range(1,N):
    if result[0]>s_list[i][0]: #현 강의의 끝나는 시간이 다음 강의의 시작하는 시간보다 클경우
        heapq.heappush(result,s_list[i][1])
    else:
        heapq.heappop(result)
        heapq.heappush(result,s_list[i][1])
        
print(len(result))