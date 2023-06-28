import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;


public class Main {
      public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        String[] A = br.readLine().split("");
        Integer[] num_list= new Integer[A.length];
        for(int i=0;i<A.length;i++){
            int num = Integer.parseInt(A[i]);
            num_list[i]=num;
        }
        Arrays.sort(num_list,Collections.reverseOrder());
        for(int i =0; i<num_list.length;i++){
            System.out.print(""+num_list[i]);
        }
    }
    
}
