import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();

        int answer = 0;

        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ('a') || word.charAt(i) == ('e') || word.charAt(i) == ('i') || word.charAt(i) == ('o') || word.charAt(i) == ('u')) answer += 1;
        }

        System.out.println(answer);
    }
}