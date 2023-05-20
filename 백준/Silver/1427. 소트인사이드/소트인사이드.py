from sys import stdin as s
#s= open("input.txt","rt")
n=list(s.readline().strip())
print("".join(sorted(n,reverse=True)))