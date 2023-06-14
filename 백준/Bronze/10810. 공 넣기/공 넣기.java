import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine()," ");
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N=Integer.parseInt(st.nextToken());
        int M =Integer.parseInt(st.nextToken());

        int[] goal_list = new int[N];
        for(int x=0; x<goal_list.length; x++){
            goal_list[x]=0;
        }

        
        for(int a =0; a<M;a++){
            st = new StringTokenizer(bf.readLine()," ");
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            while(i<=j){
                goal_list[i-1] = k;
                i++;
            }
        }
        
        for(int k=0; k< goal_list.length; k++){
            bw.write(goal_list[k]+" ");
        }
        bf.close();
        bw.flush();
        bw.close();

    }
    
}
