import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNext()){
            int time = scanner.nextInt();
            while(time-- > 0){
                int n = scanner.nextInt();
                int re1 = 0, re2 = 0;
                for(int i = 0; i < n; i++){
                    if(i == 0){
                        re1 = scanner.nextInt();
                    }
                    else{
                        re1 = re1 ^ scanner.nextInt();
                    }
                }
                for(int i = 0; i < n - 1; i++){
                    if(i == 0){
                        re2 = scanner.nextInt();
                    }
                    else{
                        re2 = re2 ^ scanner.nextInt();
                    }
                }
                System.out.println(re1 ^ re2);
            }
        }
    }
}