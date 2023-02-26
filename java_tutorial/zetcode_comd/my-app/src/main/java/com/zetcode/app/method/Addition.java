package com.zetcode.app.method;

class AddValues {
    public  int addTwoValues(int x, int y) {
        return x + y;
    }

    public int addThreeValues(int x, int y, int z) {
        return x + y + z;
    }
}

public class Addition {

    public static void main(String[] args) {

        AddValues a = new AddValues();
        int x = a.addTwoValues(12, 13);
        int y = a.addThreeValues(12, 13, 14);

        System.out.println(x);
        System.out.println(y);
    }
}
