import java.io.*;
import java.lang.*;
import java.math.*;
import java.util.*;

public class A_guy_with_a_mental_problem {

    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int t = scan.nextInt();
      while (t-- > 0) {
        int n = scan.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
          a[i] = scan.nextInt();
        }
        for (int i = 0; i < n; i++) {
          b[i] = scan.nextInt();
        }
        long sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
          if (i % 2 == 0) {
            sumA = sumA + (long) a[i];
          } else {
            sumA = sumA + (long) b[i];
          }
        }
        for (int i = 0; i < n; i++) {
          if (i % 2 == 0) {
            sumB = sumB + (long) b[i];
          } else {
            sumB = sumB + (long) a[i];
          }
        }
        sumA = Math.min(sumA, sumB);
        System.out.println(sumA);
      }
    }
  }