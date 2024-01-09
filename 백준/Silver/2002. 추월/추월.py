import sys
from collections import deque
N = int(sys.stdin.readline())
#대근 - 터널의 입구
#영식 - 터널의 출구
start=deque()
for i in range(N):
    car = sys.stdin.readline().strip()
    start.append(car)
count=0
for j in range(N):
    end_car=sys.stdin.readline().strip()
    p = start.popleft()
    if p!=end_car:
        count+=1
        start.appendleft(p)
        start.remove(end_car)
    else:
        continue
print(count)

