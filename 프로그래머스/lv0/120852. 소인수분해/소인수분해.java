import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n];
        List<Integer> result = new ArrayList<>();
        int i=2;

        while(n>=2){
            if(n%i==0){
                result.add(i);
                n=n/i;
            }
            else{
                i++;
            }
        }
        
        answer = result.stream().distinct().mapToInt(Integer::intValue).toArray();
        
        return answer;
        
    }
}
