import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] num_list = new int[N];

        for(int k=0;k<N;k++){
            num_list[k]=k+1;
        }

        for(int a=0;a<M;a++){
            int temp=0;
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            i-=1;
            j-=1;
            temp=num_list[i];
            num_list[i]=num_list[j];
            num_list[j]=temp;
        }

        for(int z=0; z<num_list.length;z++){
            bw.write(num_list[z]+" ");
        }
        bw.flush();
        bw.close();
    }
}
