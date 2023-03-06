package com.zetcode.app.statickeyword;

import java.util.ArrayList;
import java.util.List;

class Being {
    public static int count;
}

class Cat extends Being {
    public Cat() {
        count++;
    }
}

class Dog extends Being {
    public Dog() {
        count++;
    }
}

class Donkey extends Being {
    public Donkey() {
        count++;
    }
}

public class JavaStaticVariable {

    public static void main(String[] args) {
        List<Being> beings = new ArrayList() {{
           add(new Cat());
           add(new Cat());
           add(new Cat());
           add(new Dog());
           add(new Donkey());
        }};

        int nOfBeings = Being.count;

        System.out.printf("There are %d beings %n", nOfBeings);


    }
}
