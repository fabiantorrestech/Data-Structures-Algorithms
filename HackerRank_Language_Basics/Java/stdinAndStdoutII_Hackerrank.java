// problem: https://www.hackerrank.com/challenges/java-stdin-stdout/problem?isFullScreen=true

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        // Write your code here.
        Double d = scan.nextDouble();
        scan.nextLine();                // clear the buffer from nextInt() input queue buffer.
        String s = scan.nextLine();     // read in entire string with spaces.
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
