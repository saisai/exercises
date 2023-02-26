package com.zetcode.app;

import java.util.Scanner;

public class ReadLine {

    public static void main(String[] args) {
        System.out.print("Write you name:");
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();

        System.out.println("Hello " + name);
    }
}
