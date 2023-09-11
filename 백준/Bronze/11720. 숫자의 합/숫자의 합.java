import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        String sNum = br.readLine();
        char[] cNum = sNum.toCharArray();

        int sum=0;
        for(int i=0; i<cNum.length; i++){
            sum+=(cNum[i]-48);
        }

        System.out.println(sum);

    }

}
