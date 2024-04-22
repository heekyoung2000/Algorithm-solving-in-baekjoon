import sys

input = sys.stdin.readline
def recursive(length,start,s_list):
    if length==1:
        return s_list
    else:
        length=length//3
        for i in range(start+length,start+length*2):
            s_list[i]=" "
        recursive(length,start,s_list)
        recursive(length,start+length*2,s_list)
    
    
while True:
    try:
        N = int(input())
        s_list = ['-']*(3**(N))
        recursive(len(s_list),0,s_list)
        print(''.join(s_list)) 
    except:
        break