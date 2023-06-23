import java.util.*;

class Solution {
    public String solution(String s) {
        String s_array[] = s.split("");
        String result = "";
        int count = 0;
        
        Arrays.sort(s_array);
        for(int i=0; i<s_array.length; i++){
            count=0;
            for(int j=0; j<s_array.length; j++){
                if(s_array[i].equals(s_array[j])){
                    count++;
                }
            }
            if(count==1){
                result+=s_array[i];
            }
        }
        return result;
    }
}