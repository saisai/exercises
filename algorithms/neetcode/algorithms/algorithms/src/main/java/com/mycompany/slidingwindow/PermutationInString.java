package com.mycompany.slidingwindow;

public class PermutationInString {
    public boolean isEmpty(int[] arr) {
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != 0) return false;
        }
        return true;
    }

    public boolean checkInclusion(String s1, String s2) {
    //static boolean checkInclusion(String s1, String s2) {
        if(s2.length() < s1.length()) return false;
        int[] arr = new int[26];
        // add the values to the hash array
        for(int i=0; i < s1.length(); i++) {
            arr[s1.charAt(i) - 'a']++;
        }

        int i = 0;
        int j = 0;
        // point j to it's position
        for(; j < s1.length(); j++) {
            arr[s2.charAt(j) - 'a']--;
        }
        j--;
        if(isEmpty(arr)) return true;
        while(j < s2.length()) {
            arr[s2.charAt(i) - 'a']++;
            i++;
            j++;
            if(j < s2.length()) arr[s2.charAt(j) - 'a']--;
            if(isEmpty(arr)) return true;
        }
        return isEmpty(arr);
     }

     public static void main(String... args) {
         String s1 = "ab", s2 = "eidbaooo";
         PermutationInString obj = new PermutationInString();
         System.out.println(obj.checkInclusion(s1, s2));
         //System.out.println(checkInclusion(s1, s2));
     }
}
