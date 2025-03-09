import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int burger = 2000;
        int drink = 2000;

        for (int i = 0; i < 3; i++) {
            burger = Math.min(sc.nextInt(), burger);
        }

        for (int i = 0; i < 2; i++) {
            drink = Math.min(sc.nextInt(), drink);
        }

        System.out.println(burger + drink - 50);
    }
}