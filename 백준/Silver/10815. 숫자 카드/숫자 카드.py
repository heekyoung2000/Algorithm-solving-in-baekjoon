from sys import stdin as s

N = int(s.readline())
have_list = set(map(int, s.readline().split()))
M = int(s.readline())
num_list = list(map(int,s.readline().split()))
result_list = []

for num in num_list:
    if num in have_list:
        result_list.append(1)
    else:
        result_list.append(0)

print(*result_list)
    