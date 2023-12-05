package com.mycompany.leetcode.grind75.week1.ValidParentheses;

import java.util.Stack;

public class ValidParenthesesVikasPathak123 {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(char c : s.toCharArray()) {
            if(c == '(')
                stack.push(')');
            else if(c == '{')
                stack.push('}');
            else if(c == '[')
                stack.push(']');
            else if(stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }

    public boolean isValid2(String s) {
        Stack<Character> stack = new Stack<Character>();

        for(char c : s.toCharArray()) {
            if(c == '(' || c == '[' || c == '{')
                stack.push(c);
            else {
                if(stack.isEmpty()) {
                    return false;
                }
                char top = stack.peek();
                if((c == ')' && top == '(') || ( c == ']' && top == '[') || (c == '}' && top == '{')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "()[]{}";
        ValidParenthesesVikasPathak123 obj = new ValidParenthesesVikasPathak123();
        System.out.println(obj.isValid(s));

        System.out.println(obj.isValid2(s));
    }
}
