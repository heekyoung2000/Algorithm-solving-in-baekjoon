while True:
    try:
        N=int(input())
    except EOFError:
        break
    
    a,i=0,0
    while True:
        a+=10**i
        if a%N==0:
            print(i+1)
            break
        else:
            i+=1