# 멀티탭 
from sys import stdin as s

#s=open("input.txt","rt")
n,k=map(int,s.readline().split())
muti_list=list(map(int,s.readline().split()))
muti_tap=[0]*n
ans=0
maximum=0
while muti_list:
    product = muti_list[0]
    if product in muti_tap: #멀티탭에 같은 번호가 꽂혀져 있으면 그냥 무시
        muti_list.remove(product)
        continue
    elif 0 in muti_tap:
        muti_tap[muti_tap.index(0)]=product
        muti_list.remove(product)
        
    else:
        for mt in muti_tap:
            if mt not in muti_list:
                change=mt
                break
            
            elif muti_list.index(mt) > maximum:
                maximum = muti_list.index(mt)
                change=mt
                
        muti_tap[muti_tap.index(change)]=product
        muti_list.remove(product)
        maximum=0
        ans+=1
        
        
print(ans)