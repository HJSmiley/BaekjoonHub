import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < N; i++) {
            String pw = sc.nextLine();
            int len = pw.length();

            if (len >= 6 && len <= 9) {
                System.out.println("yes");
            }
            else {
                System.out.println("no");
            }
        }
    }
}