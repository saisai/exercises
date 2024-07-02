package org.example;

public class PalindromeString {
    private static void checkPalindromeString(String input) {
        boolean result = true;
        int lenght = input.length();
        for(int i = 0; i < lenght /2; i++) {
            if(input.charAt(i) != input.charAt(lenght-i-1)) {
                result = false;
                break;
            }
        }

        System.out.println(input + " is palindrome = "+result);
    }

    public static void main(String[] args) {
        checkPalindromeString("abc");
        checkPalindromeString("abcba");
        checkPalindromeString("ç∂©∂ç");
    }
}
