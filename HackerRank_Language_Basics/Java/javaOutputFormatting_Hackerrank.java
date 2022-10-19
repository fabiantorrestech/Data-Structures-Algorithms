// problem: https://www.hackerrank.com/challenges/java-output-formatting/problem?isFullScreen=true

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                System.out.printf("%-15s%03d\n", s1, x);    // %s = string
                                                            // %d = int
                                                            // %-15s = left-justified string by 15 chars.
                                                            // %03d = 3 digit integer. pad with zeroes in beginning.
                
            }
            System.out.println("================================");

    }
}