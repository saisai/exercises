package com.example.learnjava.util.map;

import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class HashMapDemo {
    public static void main (String[]args) {
        HashMap<Integer, String> hm = new HashMap<Integer, String>();
        hm.put(11, "Sachin");
        hm.put(37, "Dhoni");
        hm.put(25, "Kohli");
        hm.put(13, "Raina");
        hm.put(12, "Yuvraj");
        System.out.println(hm);
        System.out.println(hm.size());
        Set ks = hm.keySet();
        System.out.println(ks);
        Collection cv = hm.values ();
        System.out.println (cv);
        Set entry = hm.entrySet ();
        System.out.println (entry);
        System.out.println (hm.containsKey (12));
        System.out.println (hm.remove (25));
        System.out.println (hm);
    }
}

// https://dotnettutorials.net/lesson/map-collections-in-java/