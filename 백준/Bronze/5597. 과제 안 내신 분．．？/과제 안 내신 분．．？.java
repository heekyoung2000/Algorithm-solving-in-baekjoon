import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        int[] student_list = new int[31];
        boolean[] ans_list = new boolean[31];
        for(int i=1; i<=28; i++){
            int n= Integer.parseInt(br.readLine());
            ans_list[n]=true;
        }
        Arrays.sort(student_list);

        for (int i = 1; i <= 30; i++) {
            if (!ans_list[i]) System.out.println(i);  //불리지 않은 사람 출력
        }
    }

}

