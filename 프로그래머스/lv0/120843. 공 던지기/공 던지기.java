class Solution {
    public int solution(int[] numbers, int k) {
        
        
        int count=1;
        int index=0;
        
        while(count!=k){
            index+=2;
            count++;
            if(index>=numbers.length){
                index-=numbers.length;
            }
        }
        return numbers[index];
    }
}