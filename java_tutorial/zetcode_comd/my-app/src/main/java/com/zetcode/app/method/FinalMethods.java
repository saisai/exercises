package com.zetcode.app.method;

class BaseFour {

    public void f1() {

        System.out.println("f1 of the Base");
    }

    public final void f2() {

        System.out.println("f2 of the Base");
    }
}


class DerivedFour extends BaseFour {

    @Override
    public void f1() {

        System.out.println("f1 of the Derived");
    }

//    @Override
//    public void f2() {
//
//        System.out.println("f2 of the Derived");
//    }
}
public class FinalMethods {

    public static void main(String[] args) {

        BaseFour b = new BaseFour();
        b.f1();
        b.f2();

        DerivedFour d = new DerivedFour();
        d.f1();
        d.f2();
    }
}
