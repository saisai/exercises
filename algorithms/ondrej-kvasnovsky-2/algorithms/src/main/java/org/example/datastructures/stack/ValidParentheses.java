package org.example.datastructures.stack;

import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if(stack.isEmpty()) {
                    return false;
                }
                char previous = stack.pop();
                if(previous == '(') {
                    if(c != ')')
                        return false;
                }
                if (previous == '[') {
                    if (c != ']')
                        return false;
                }
                if (previous == '{') {
                    if (c != '}')
                        return false;
                }
            }

        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidParentheses obj = new ValidParentheses();
        String input = "()[]{}";
        System.out.println(obj.isValid(input));
    }
}


// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/stack/valid-parentheses