package com.mycompany.leetcode.TopInterview150.stack.EvaluateReversePolishNotation;

import java.util.Stack;

public class EvaluateReversePolishNotation150pvaldes {
    public int evalRPN(String[] tokens) {
        int a, b;
        Stack<Integer> S = new Stack<Integer>();
        for(String s : tokens) {
            if(s.equals("+")) {
                S.add(S.pop() + S.pop());
            } else if(s.equals("/")) {
                b = S.pop();
                a = S.pop();
                S.add(a / b);
            } else if(s.equals("*")) {
                S.add(S.pop() * S.pop());
            } else if(s.equals("-")) {
                b = S.pop();
                a = S.pop();
                S.add(a - b);
            } else {
                S.add(Integer.parseInt(s));
            }
        }
        return S.pop();
    }

    public static void main(String[] args) {
        String[] tokens = {"4","13","5","/","+"};
        EvaluateReversePolishNotation150pvaldes obj = new EvaluateReversePolishNotation150pvaldes();
        System.out.println(obj.evalRPN(tokens));
    }
}
