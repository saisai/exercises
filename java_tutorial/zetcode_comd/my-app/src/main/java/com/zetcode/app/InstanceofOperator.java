package com.zetcode.app;

import java.awt.dnd.DragGestureEvent;

class Base {}
class Derived extends Base {}

public class InstanceofOperator {

    public static void main(String[] args) {
        Base b = new Base();
        Derived d = new Derived();

        System.out.println(d instanceof Base);
        System.out.println(b instanceof Derived);
        System.out.println(d instanceof Object);
    }
}
