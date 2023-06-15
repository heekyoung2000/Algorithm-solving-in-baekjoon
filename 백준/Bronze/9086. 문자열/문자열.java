import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        String result[] = new String[T];
        for(int i =0; i<T; i++){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            
            String arr[] = s.split("");
            result[i]=arr[0]+arr[arr.length-1];
        }

        for(int j=0; j<result.length; j++){
            System.out.println(result[j]);
        }
    
    }
}
