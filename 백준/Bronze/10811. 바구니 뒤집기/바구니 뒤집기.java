import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out)); 

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[] bool_list = new int[N];

        for(int q=0;q<N; q++){
            bool_list[q]=q+1;
        }

        
        for(int k=0; k<M; k++){
            st = new StringTokenizer(br.readLine());
            int temp=0;
            int i= Integer.parseInt(st.nextToken());
            int j= Integer.parseInt(st.nextToken());
            
            
            i-=1;
            j-=1;
            while(i<j){
                temp = bool_list[i];
                bool_list[i]=bool_list[j];
                bool_list[j]=temp;
                
                i++;
                j--;
            }
        
        }

        for(int x=0; x<bool_list.length; x++){
            wr.write(bool_list[x]+" ");
        }
        wr.flush();
        wr.close();
    }
    
}
