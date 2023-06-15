import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out)); 

        String word = st.nextToken();
        String [] word_list = word.split("");
        int time=0;
        
        for(int i=0; i< word_list.length;i++){
            String w = word_list[i];
            switch(w){
                case "A": case "B": case "C":
                    time+=3;
                    break;
                case "D": case "E": case "F":
                    time+=4;
                    break;
                case "G": case "H": case "I":
                    time+=5;
                    break;
                case "J": case "K": case "L":
                    time+=6;
                    break;
                case "M": case "N": case "O":
                    time+=7;
                    break;
                case "P": case "Q": case "R": case "S":
                    time+=8;
                    break;
                case "T": case "U": case "V":
                    time+=9;
                    break;
                case "W": case "X": case "Y": case "Z":
                    time+=10;
                    break;


            }
        }

        System.out.println(time);



    }
}
