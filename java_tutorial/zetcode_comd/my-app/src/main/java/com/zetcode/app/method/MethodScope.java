package com.zetcode.app.method;

class Test {

    int x = 1;

    public void exec1() {

        System.out.println(this.x);
        System.out.println(x);
    }

    public void exec2() {

        int z = 5;

        System.out.println(x);
        System.out.println(z);
    }
}

public class MethodScope {
    public static void main(String[] args) {

        Test ts = new Test();
        ts.exec1();
        ts.exec2();
    }
}
