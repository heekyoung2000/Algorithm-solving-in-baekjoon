import sys
input =sys.stdin.readline

name = input().strip()
n= int(input())
winner_list = []
team_list = [] 
for _ in range(n):
    team_name=input().strip()
    s = name + team_name
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    num = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    winner_list.append((num,team_name))
winner_list.sort(key = lambda x : (-x[0],x[1]))

print(winner_list[0][1])

