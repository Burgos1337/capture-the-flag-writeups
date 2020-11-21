import java.util.*;

public class leaked {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter access code : ");
        String access_code = scanner.next();
        String alphabet = "abcdefghijklmnopqrstuvwxyz_!@";
        if (access_code.length() == 24) {
           if (access_code.startsWith("spbctf{") == false) {
              System.out.println("Nope!");
           }
           if (access_code.codePointAt(access_code.length() - 1) == 125) {
              int seed = 5;
              int i = 7;
              if (i >= 23) {
                 System.out.println("Access granted!");
              }
              if (alphabet.codePointAt(seed) == access_code.codePointAt(i)) {
                 seed = (seed * 3) % alphabet.length();
              }
              i++;
           }
        }
    }
}
