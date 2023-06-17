import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        double count=0;
        double credit_count=0;
        double num_grade=0;
        
        for(int i=0; i< 20; i++){
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            String subject = st.nextToken();
            double credit = Double.parseDouble(st.nextToken());
            String grade = st.nextToken();
        
         
            switch(grade){
                case "A+":
                    num_grade=4.5;
                    break;
                case "A0":
                    num_grade=4.0;
                    break;
                case "B+":
                    num_grade=3.5;
                    break;
                case "B0":
                    num_grade=3.0;
                    break;
                case "C+":
                    num_grade=2.5;
                    break;
                case "C0":
                    num_grade=2.0;
                    break;
                case "D+":
                    num_grade=1.5;
                    break;
                case "D0" :
                    num_grade=1.0;
                    break;
                case "F":
                    num_grade=0.0;
                    break;
                case "P":
                    num_grade=0.0;
                    credit_count-=credit;

            }
                count+=credit*num_grade;
                credit_count+=credit;
        }
        double average = count/credit_count;
        System.out.printf("%.6f",average);
    }
}
