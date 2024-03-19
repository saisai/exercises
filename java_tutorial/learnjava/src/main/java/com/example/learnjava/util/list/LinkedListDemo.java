package com.example.learnjava.util.list;

import java.util.Iterator;
import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> animals = new LinkedList<>();

        animals.add("Dog");
        animals.add("Cat");
        animals.add("Horse");
        animals.add("Hawk");

        System.out.println("LinkedList: " + animals);

        String str = animals.get(1);
        System.out.println("Element at index 1: " + str);
        System.out.println(" ");

        for (String animal : animals) {
            System.out.println(animal);
        }

        Iterator<String> itr = animals.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next());
        }
    }
}


// https://dotnettutorials.net/lesson/list-collections-in-java/