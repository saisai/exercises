package org.example.digitaloceancom.javaset;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class SetIteratorExample {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<5; i++)
            set.add(i);

        Iterator iterator = set.iterator();

        //simple iteration
        while(iterator.hasNext()){
            int i = (int) iterator.next();
            System.out.print(i + ", ");
        }
        System.out.println("\n" + set);

        //modification of set using iterator
        iterator = set.iterator();
        while(iterator.hasNext()){
            int x = (int) iterator.next();
            if(x%2 ==0) iterator.remove();
        }
        System.out.println(set);

        //changing set structure while iterating
        iterator = set.iterator();
        while(iterator.hasNext()){
            //ConcurrentModificationException here
            int x = (int) iterator.next();
            if(x==1) set.add(10);
        }
    }
}
