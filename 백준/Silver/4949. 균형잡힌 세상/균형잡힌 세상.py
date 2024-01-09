import sys
from collections import deque
opener = {
    "(":")",
    "[":"]",
    ")":"(",
    "]":"["

}

while True:
    m = input()
    d = []

    if m==".":
        break
    for i in m:
        if i=="(" or i=="[":
            d.append(i)
        elif i=="]":
            if len(d)!=0 and d[-1]=="[":
                d.pop()
            else:
                d.append(']')
                break
        elif i==")":
            if len(d)!=0 and d[-1]=="(":
                d.pop()
            else:
                d.append(')')
                break
    
    if len(d)==0:
        print("yes")    
    else:
        print("no")
