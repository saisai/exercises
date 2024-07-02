package org.example;

import java.util.Scanner;

public class SwapTwoStrings {

    static class Container{
        private String firstString;
        private String secondString;

        public String getFirstString() {
            return firstString;
        }
        public void setFirstString(String firstString) {
            this.firstString = firstString;
        }
        public String getSecondString() {
            return secondString;
        }
        public void setSecondString(String secondString) {
            this.secondString = secondString;
        }

        @Override
        public String toString() {
            return "First String = "+firstString+", Second String = "+secondString;
        }
    }
    public static void main(String[] args) {

        Container container = new Container();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter First String:");
        container.setFirstString(scanner.nextLine());

        System.out.println("Enter Second String:");
        container.setSecondString(scanner.nextLine());
        scanner.close();
        System.out.println(container);
        container = swapStrings(container);
        System.out.println(container);
    }

    private static Container swapStrings(Container container) {
        container.setFirstString(container.getFirstString().concat(container.getSecondString())); //s1 = s1+s2
        container.setSecondString(container.getFirstString().substring(0, container.getFirstString().length()-container.getSecondString().length())); // s2=s1
        container.setFirstString(container.getFirstString().substring(container.getSecondString().length()));
        return container;
    }
}
