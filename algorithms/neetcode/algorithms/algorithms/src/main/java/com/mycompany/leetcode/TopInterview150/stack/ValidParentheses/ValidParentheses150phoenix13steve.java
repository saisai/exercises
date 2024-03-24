package com.mycompany.leetcode.TopInterview150.stack.ValidParentheses;

import java.util.Stack;

public class ValidParentheses150phoenix13steve {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if(c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if(c == '[') {
                stack.push(']');
            } else if(stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "()[]{}";
        ValidParentheses150phoenix13steve obj = new ValidParentheses150phoenix13steve();
        System.out.println(obj.isValid(s));
    }
}
