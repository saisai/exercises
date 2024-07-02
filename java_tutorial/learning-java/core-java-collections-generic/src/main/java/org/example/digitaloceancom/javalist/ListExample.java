package org.example.digitaloceancom.javalist;

import java.util.ArrayList;
import java.util.List;

public class ListExample {

        public static void main(String args[]) {
            List<String> vowels= new ArrayList<>();

            //add example
            vowels.add("A");
            vowels.add("I");

            //let's insert E between A and I
            vowels.add(1,"E");
            System.out.println(vowels);

            List<String> list = new ArrayList<String>();
            list.add("O");list.add("U");

            //appending list elements to letters
            vowels.addAll(list);
            System.out.println(vowels);

            //clear example to empty the list
            list.clear();

            //size example
            System.out.println("letters list size = "+vowels.size());

            //set example
            vowels.set(2, "E");
            System.out.println(vowels);

            //subList example
            vowels.clear();vowels.add("E"); vowels.add("E");vowels.add("I"); vowels.add("O");
            list = vowels.subList(0, 2);
            System.out.println("letters = "+vowels+", list = "+list);
            vowels.set(0, "A");
            System.out.println("letters = "+vowels+", list = "+list);
            list.add("U");
            System.out.println("letters = "+vowels+", list = "+list);



    }
}
