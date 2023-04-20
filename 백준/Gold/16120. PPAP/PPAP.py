import sys

n=(sys.stdin.readline().strip())

stack=[]
for i in range(len(n)):
    stack.append(n[i])
    if len(stack)>=4 and stack[-1]=="P" and stack[-2]=="A" and stack[-3]=="P":
        stack.pop()
        stack.pop()
        stack.pop()
    
        
if stack==['P']:
    print("PPAP")
else:
    print("NP")