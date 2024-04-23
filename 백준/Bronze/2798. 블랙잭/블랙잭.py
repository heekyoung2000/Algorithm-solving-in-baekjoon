import sys
from itertools import combinations

input = sys.stdin.readline

N,M = map(int,input().split())
card = list(map(int,input().split()))

result = 0
for comcard in list(combinations(card,3)):
    if sum(comcard)>M:
        continue
    else:
        result = max(result,sum(comcard))

print(result)