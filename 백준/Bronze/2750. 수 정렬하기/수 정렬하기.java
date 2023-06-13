import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        
        int N= Integer.parseInt(bf.readLine());
        int [] number = new int[N];

        for(int i=0; i<N; i++){
            number[i] = Integer.parseInt(bf.readLine());
        }
        Arrays.sort(number);
        for(int j=0;j<number.length; j++){
            System.out.println(number[j]);
        }
        
    }
    
}