package com.mycompany.leetcode.blind75.string.ValidParentheses;


import java.util.Stack;

public class ValidParenthesesPhoenix13steve {
    static boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(char c : s.toCharArray()) {
            if(c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "()[]{}";
        System.out.println(isValid(s));
    }
}
