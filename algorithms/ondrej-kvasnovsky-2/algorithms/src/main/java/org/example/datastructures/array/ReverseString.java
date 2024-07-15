package org.example.datastructures.array;

public class ReverseString {
    public String reverseString(String s) {
        int start = 0;
        int end = s.length() - 1;
        char[] chars = new char[s.length()];
        while(start <= end) {
            char startVal = s.charAt(start);
            char endVal = s.charAt(end);
            chars[start] = endVal;
            chars[end] = startVal;
            start++;
            end--;
        }
        return new String(chars);
    }

    public String reverseString2(String s) {
        int start = 0;
        int end = s.length() - 1;
        char[] chars = s.toCharArray();
        while(start <= end) {
            char temp = chars[start];
            chars[start] = chars[end];
            chars[end] = temp;
            start++;
            end--;
        }
        return new String(chars);
    }

    public static void main(String[] args) {
        String givenString = "hello";
        ReverseString obj = new ReverseString();
        System.out.println(obj.reverseString(givenString));
        System.out.println(obj.reverseString2(givenString));
    }
}

// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/array/reverse-string