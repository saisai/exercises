package com.zetcode.app.method;

class Sum {

    public int getSum() {

        return 0;
    }

    public int getSum(int x) {

        return x;
    }

    public int getSum(int x, int y) {

        return x + y;
    }
}

public class Overloading {
    public static void main(String[] args) {

        Sum s = new Sum();
        System.out.println(s.getSum());
        System.out.println(s.getSum(5));
        System.out.println(s.getSum(5, 10));
    }
}
