import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            double n = sc.nextDouble();
            String s = sc.next();

            if (s.equals("kg")) {
                n *= 2.2046;
                s = "lb";
            }
            else if (s.equals("lb")) {
                n *= 0.4536;
                s = "kg";
            }
            else if (s.equals("l")) {
                n *= 0.2642;
                s = "g";
            }
            else {
                n *= 3.7854;
                s = "l";
            }

            String res = String.format("%.4f", n) + " " + s;
            System.out.println(res);
        }
    }
}