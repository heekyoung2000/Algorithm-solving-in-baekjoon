import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        

        int N=Integer.parseInt(bf.readLine());
        int [] num_list = new int[N]; 
        int count =0;
        StringTokenizer st = new StringTokenizer(bf.readLine()," ");
        for(int i=0; i<N; i++){
            num_list[i]=Integer.parseInt(st.nextToken());
        }

        int V=Integer.parseInt(bf.readLine());

        for(int j=0; j<num_list.length; j++){
            if(num_list[j]==V){
                count++;
            }
        }

        System.out.println(count);

    }
    
}
