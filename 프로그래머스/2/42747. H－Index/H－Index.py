def solution(citations):
    k=len(citations)
    
    def sorted(new_arr):
        result=[]
        new_arr.sort()
        left=0
        right=new_arr[-1]
        while left<right:
            mid=(left+right)//2
            count=0
            left_count=0
            for r in new_arr:
                if r>=mid:
                    count+=1
                else:
                    left_count+=1   
            #mid번 이상 인용된 논문이 mid편이상 & 나머지 논문이 mid 이하 
            if count==mid and left_count==k-count:
                result.append(mid)
                left+=1
            elif count<mid:#mid번 이상 인용된 논문이 mid편 미만일 경우
                right-=1
            else:#mid번 이상 인용된 논문이 mid편 초과일 경우
                left+=1
        if result==[]:
            return left-1
        else:
            return result[-1]
            
    
    
    if k==1:
        if citations[0]==1:
            return 1
        else:
            return 0
    elif len(set(citations))==1:
        return citations[0]
    else:
        return sorted(citations)
        