def solution(s):
    zero_count,two_count=0,0
    while len(s)!=1:
        new_s=""
        for i in s:
            if i=="1":
                new_s+="1"
            else:
                zero_count+=1
        n_s=bin(len(new_s))
        s=n_s[2:]
        two_count+=1
    return [two_count,zero_count]