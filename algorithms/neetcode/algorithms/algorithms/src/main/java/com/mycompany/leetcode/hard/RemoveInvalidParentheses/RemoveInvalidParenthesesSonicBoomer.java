package com.mycompany.leetcode.hard.RemoveInvalidParentheses;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RemoveInvalidParenthesesSonicBoomer {

    // The minimum deletion performed on a valid string, so far.
    static int minCount = Integer.MAX_VALUE;

    static void recurse(String s, int pos, Set<String> result, StringBuilder buffer,
                        int open, int close, int ctr) {

        if(s.length() == pos) {
            if(open == close && ctr <= minCount) {
                if(ctr == minCount)
                    result.add(buffer.toString());
                else {
                    result.clear();
                    minCount = ctr;
                    result.add(buffer.toString());
                }
            }
            return;
        }

        if(close > open)
            return;

        if(s.length() - pos < open - close)
            return;

        char c = s.charAt(pos);
        if(c == '(') {
            buffer.append(c);
            recurse(s, pos + 1, result, buffer, open + 1, close, ctr);
            buffer.deleteCharAt(buffer.length() - 1);

            recurse(s, pos + 1, result, buffer, open, close, ctr + 1);
        } else if( c == ')') {
            buffer.append(c);
            recurse(s, pos + 1, result, buffer, open, close + 1, ctr);
            buffer.deleteCharAt(buffer.length() - 1);

            recurse(s, pos + 1, result, buffer, open, close, ctr + 1);
        } else {
            buffer.append(c);
            recurse(s, pos + 1, result, buffer, open, close, ctr);
            buffer.deleteCharAt(buffer.length() - 1);
        }
    }

    public static List<String> removeInvalidParentheses(String s) {
        // We use a set because duplicate result strings can be generated.
        Set<String> result = new HashSet<>();
        recurse(s, 0, result, new StringBuilder(), 0, 0, 0);
        return new ArrayList<>(result);
    }
    public static void main(String[] args) {
        String s = "()())()";
        List<String> result = removeInvalidParentheses(s);

        result.forEach( e -> {
            System.out.print(e);
            for(char c : e.toCharArray()) {
                System.out.print(c);
            }
            System.out.println();
        });

        for(String ss : result) {
            System.out.println(ss);
        }

    }

}
