import sys

input = sys.stdin.readline
def recursion(s,l,r,cnt):
    if l>=r: return 1,cnt
    elif s[l]!=s[r]: return 0,cnt
    else: 
        cnt+=1
        return recursion(s,l+1,r-1,cnt)

def isPalindrome(string):
    return recursion(string,0, len(string)-1,1)
    
N = int(input())
for _ in range(N):
    string = input().strip()
    result= isPalindrome(string)
    for r in result:
        print(r,end=" ")
    print()