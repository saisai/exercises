package com.mycompany.leetcode.TopInterview150.Backtracking.LetterCombinationsOfAPhoneNumber;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class LetterCombinationsOfAPhoneNumber150lirensun {
    public List<String> letterCobinationsFIFO(String digits) {
        LinkedList<String> ans = new LinkedList<String>();
        if(digits.isEmpty()) return ans;
        String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        ans.add("");
        for(int i = 0; i < digits.length(); i++) {
            int x = Character.getNumericValue(digits.charAt(i));
            while(ans.peek().length() == i) {
                String t = ans.remove();
                for(char s : mapping[x].toCharArray()) {
                    ans.add(t+s);
                }
            }
        }
        return ans;
    }

    public List<String> letterCombinationsBFS(String digits) {
        LinkedList<String> ans = new LinkedList<String>();
        if(digits.isEmpty()) return ans;
        String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        ans.add("");
        while(ans.peek().length() != digits.length()) {
            String remove = ans.remove();
            String map = mapping[digits.charAt(remove.length()) - '0'];
            for(char c : map.toCharArray()) {
                ans.addLast(remove + c);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        String digits = "23";
        LetterCombinationsOfAPhoneNumber150lirensun obj = new LetterCombinationsOfAPhoneNumber150lirensun();
//        List<String> result = obj.letterCobinationsFIFO(digits);
        List<String> result = obj.letterCombinationsBFS(digits);
        System.out.println(String.join("\n", result));
        System.out.println(String.join(",", result));
        String test = String.join(",", result);
        System.out.println(test);
    }
}
