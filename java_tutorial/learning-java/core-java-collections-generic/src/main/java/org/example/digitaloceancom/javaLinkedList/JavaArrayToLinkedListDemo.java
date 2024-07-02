package org.example.digitaloceancom.javaLinkedList;

import java.util.LinkedList;
import java.util.List;

public class JavaArrayToLinkedListDemo {
    public static void main(String[] args)
    {
        Integer[] numbers = {1,2,3,4,5};
        List<Integer> numbersList = new LinkedList<>();
        for(Integer s : numbers){
            numbersList.add(s);
        }
        System.out.println(numbersList);
    }
}
