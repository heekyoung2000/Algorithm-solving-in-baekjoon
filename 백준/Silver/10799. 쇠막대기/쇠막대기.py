import sys
from collections import deque

q = deque()

example = list(map(str,input()))
count=0
q.append(example[0])

for i in range(1,len(example)):
    # 이전이랑 q값이 똑같을 경우
    if example[i]=="(":
        q.append(example[i])
    #레이저인 경우
    elif example[i-1]=="(" and example[i]==")":
        q.pop()
        count+=len(q)
    # 레이저가 아님 && 오른쪽 끝이 들어왔을 때
    elif example[i]==")":
        q.pop()
        count+=1
        
            
print(count)


    