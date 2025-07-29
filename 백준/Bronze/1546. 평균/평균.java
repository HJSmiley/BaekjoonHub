import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        int m = 0;
        double newM = 0;
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(sc.nextLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] > m) {
                m = arr[i];
            }
        }

        for (int i = 0; i < n; i++) {
            newM += (double) arr[i] / m * 100;
        }
        newM /= n;

        System.out.println(newM);
    }
}
