package org.example.digitaloceancom.javalist;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListToArray {
    public static void main(String[] args) {

        List<String> letters = new ArrayList<String>();

        // add example
        letters.add("A");
        letters.add("B");
        letters.add("C");

        //convert list to array
        String[] strArray = new String[letters.size()];
        strArray = letters.toArray(strArray);
        System.out.println(Arrays.toString(strArray)); //will print "[A, B, C]"
    }

}
