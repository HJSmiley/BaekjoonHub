import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 수의 개수 n과 합을 구해야 하는 횟수 m 입력
        int n = sc.nextInt();
        int m = sc.nextInt();

        // 배열 입력
        int arr[] = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }

        // 누적합 배열 생성
        int preSum[] = new int[n+1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i-1] + arr[i];
        }

        // 각 구간합 구하기
        for (int i = 0; i < m; i++) {
            // 구간 입력
            int a = sc.nextInt();
            int b = sc.nextInt();

            // 구간합 구하기
            int res = preSum[b] - preSum[a-1];

            System.out.println(res);
        }

        sc.close();
    }
}