import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String S = br.readLine();
        int N = Integer.parseInt(br.readLine());

        String arr[] = S.split("");

        bw.write(arr[N-1]);

        br.close();
        bw.flush();
        bw.close();

    }
    
}
