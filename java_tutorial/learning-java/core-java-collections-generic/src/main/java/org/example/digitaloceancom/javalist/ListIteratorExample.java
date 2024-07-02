package org.example.digitaloceancom.javalist;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ListIteratorExample {
    public static void main(String[] args) {

        List<Integer> list = new ArrayList<>();
        for(int i=0; i<5; i++) list.add(i);

        Iterator<Integer> iterator = list.iterator();

        //simple iteration
        while(iterator.hasNext()){
            int i = (int) iterator.next();
            System.out.print(i + ", ");
        }
        System.out.println("\n"+list);

        //modification of list using iterator
        iterator = list.iterator();
        while(iterator.hasNext()){
            int x = (int) iterator.next();
            if(x%2 ==0) iterator.remove();
        }
        System.out.println(list);

        //changing list structure while iterating
        iterator = list.iterator();
        while(iterator.hasNext()){
            int x = (int) iterator.next(); //ConcurrentModificationException here
            if(x==1) list.add(10);
        }
    }
}
