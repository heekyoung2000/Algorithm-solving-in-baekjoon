import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Integer maxlist[][] = new Integer[9][9];
        int max =0;
        int re_i=0;
        int re_j=0;
        for(int i=0;i<9;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<9;j++){
                maxlist[i][j]=Integer.parseInt(st.nextToken());
                if (max < maxlist[i][j]){
                    max=maxlist[i][j];
                    re_i=i;
                    re_j=j;
                }

            }
        }

        re_i++;
        re_j++;
        System.out.println(max);
        System.out.println(re_i+" "+re_j);
    }
    
}