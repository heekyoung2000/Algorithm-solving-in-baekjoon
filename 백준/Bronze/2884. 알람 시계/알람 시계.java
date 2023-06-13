import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int H=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        
    
        if(M>=45){
            M-=45;
            System.out.println(H+" "+M);
        }
        else{ // M이 45분 보다 작을때
            if (H==0){
                H=24;
            }
            H-=1;
            M+=60;
            M-=45;
            System.out.println(H+" "+M);
        }
        
        
    }
    
}
