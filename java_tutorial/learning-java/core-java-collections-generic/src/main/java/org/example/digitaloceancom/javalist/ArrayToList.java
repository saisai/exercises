package org.example.digitaloceancom.javalist;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayToList {
    public static void main(String[] args) {

        String[] vowels = {"a","e","i","o","u"};

        List<String> vowelsList = Arrays.asList(vowels);
        System.out.println(vowelsList);

        /**
         * List is backed by array, we can't do structural modification
         * Both of the below statements will throw java.lang.UnsupportedOperationException
         */
//        vowelsList.remove("e");
        //vowelsList.clear();

        //using for loop to copy elements from array to list, safe for modification of list
        List<String> myList = new ArrayList<>();
        for(String s : vowels){
            myList.add(s);
        }
        System.out.println(myList);
        myList.clear();
    }
}
