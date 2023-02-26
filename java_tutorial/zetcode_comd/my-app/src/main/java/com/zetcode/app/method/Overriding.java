package com.zetcode.app.method;

class BaseTwo {

    public void showInfo() {

        System.out.println("This is Base class");
    }
}

class DerivedTwo extends BaseTwo {

    @Override
    public void showInfo() {

        System.out.println("This is Derived class");
    }
}

public class Overriding {

    public static void main(String[] args) {

        BaseTwo[] objs = { new BaseTwo(), new DerivedTwo(),
                new BaseTwo(),
                new BaseTwo(), new BaseTwo(), new DerivedTwo() };

        for (BaseTwo obj : objs) {

            obj.showInfo();
        }
    }
}
