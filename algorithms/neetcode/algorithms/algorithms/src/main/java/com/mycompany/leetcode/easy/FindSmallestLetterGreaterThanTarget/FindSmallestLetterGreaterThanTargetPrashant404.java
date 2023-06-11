package com.mycompany.leetcode.easy.FindSmallestLetterGreaterThanTarget;

public class FindSmallestLetterGreaterThanTargetPrashant404 {

    public static char nextGreatestLetter(char[] letters, char target) {
        int low = 0;
        int high = letters.length - 1;

        if(target >= letters[high])
            return letters[0];

        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(letters[mid] > target)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return letters[low];
    }

    public static void main(String[] args) {
        char[] letters = {'c','f','j'};
        char target = 'a';
        System.out.println(nextGreatestLetter(letters, target));
    }

}
