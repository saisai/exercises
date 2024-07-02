package com.mycompany.leetcode.TopInterview150.stack.SimplifyPath;

import java.util.Arrays;
import java.util.Stack;
import java.util.stream.Stream;

public class SimplifyPath150himalik {
    public String simplifyPath(String path) {
        Stack<String> s = new Stack<>();
        StringBuilder sb = new StringBuilder();
        String[] p = path.split("/");

        System.out.println(p.length);
        System.out.println(Arrays.toString(p));
        Stream aa = Stream.of(p);
        aa.forEach(a -> { System.out.println(a);});
        for(int i = 0; i < p.length; i++) {
            if(!s.isEmpty() && p[i].equals("..")) s.pop();
            else if(!p[i].equals("") && !p[i].equals(".") && !p[i].equals("..")) {
                s.push(p[i]);
            }
        }

        if(s.isEmpty()) return "/";
        while(!s.isEmpty()) {

            sb.insert(0, s.pop()).insert(0, "/");
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String path = "/home//foo/";
        SimplifyPath150himalik obj = new SimplifyPath150himalik();
        System.out.println(obj.simplifyPath(path));
    }
}
