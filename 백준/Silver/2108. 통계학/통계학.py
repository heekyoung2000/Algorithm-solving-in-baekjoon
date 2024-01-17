import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
list1=[]
for i in range(N):
    num = int(sys.stdin.readline().strip())
    list1.append(num)

list1.sort()
print(round(sum(list1)/N))
print(list1[len(list1)//2])
cnt = Counter(list1).most_common(2)
if len(list1)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(list1)-min(list1))