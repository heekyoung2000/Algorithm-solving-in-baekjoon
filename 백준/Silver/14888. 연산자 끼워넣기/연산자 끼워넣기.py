import sys
input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int,input().split()))
add,sub,mul,div  = map(int,input().split())
mx,mn= int(-1e9),int(1e9)

def DFS(index,result,add,sub,mul,div):
    ##종료조건
    global mx,mn
    if result< int(-1e9) or int(1e9)<result:
        return 
    if index==N:
        mx = max(result,mx)
        mn = min(result,mn)
        return
    
    if add>0:
        DFS(index+1,result+num_list[index],add-1,sub,mul,div)
    if sub>0:
        DFS(index+1,result-num_list[index],add,sub-1,mul,div)
    if mul>0:
        DFS(index+1,result*num_list[index],add,sub,mul-1,div)
    if div>0:
        DFS(index+1,int(result/num_list[index]),add,sub,mul,div-1)
DFS(1,num_list[0],add,sub,mul,div)
print(mx,mn,sep="\n")