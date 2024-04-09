import sys
input = sys.stdin.readline

word = list(map(str,input().strip().upper()))

dic = {}
for w in word:
    if w in dic:
        dic[w]+=1
    else:
        dic[w]=1

m=-1
new_word = ""
status =False

for key,value in dic.items():
    if value>m:
        m=value
        new_word=key
        status=False
    elif value == m and new_word!=key:
        status = True

if status==False: print(new_word)
else: print("?")
    