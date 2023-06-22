class Solution {
    public String solution(String bin1, String bin2) {
        int intNum1 = Integer.parseInt(bin1,2);
        int intNum2 = Integer.parseInt(bin2,2);
        
        int result = intNum1+intNum2;
        String result_fin = Integer.toBinaryString(result);
        return result_fin;
    }
}