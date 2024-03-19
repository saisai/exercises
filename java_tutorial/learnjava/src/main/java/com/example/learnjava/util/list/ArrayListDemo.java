package com.example.learnjava.util.list;

import java.util.ArrayList;
import java.util.List;
public class ArrayListDemo
{
    public static void main (String[]args)
    {
        // Creation of ArrayList
        ArrayList <Integer> al = new ArrayList <Integer>();

        //adding the elements into the list
        al.add (10);  //autoboxing
        al.add (new Integer (20)); //manual boxing
        al.add (30);
        al.add (40);
        al.add (50);

        //Display elements of the List and its Size
        System.out.println (al);
        System.out.println (al.size ());

        //inserting an element into the List at specified location
        al.add (1, 77);
        System.out.println (al);
        System.out.println (al.size ());

        //modifying the existing element of the List by specifying its value
        al.remove (new Integer (30));
        System.out.println (al);
        System.out.println (al.size ());

        //removing the element of the List by specifying its index position
        al.remove (0);
        System.out.println (al);
        System.out.println (al.size ());

        //Displaying elements of List 1 by 1 using for loop (accessing)
        for (int i = 0; i < al.size (); i++)
        {
            System.out.println (al.get (i));
        }

        //Displaying elements of List 1 by 1 using forEach Loop (auto-unboxing)
        for (int v:al)
        {
            System.out.println (v);
        }

        //Searching an element
        System.out.println (al.contains (50));

        //Copying the array list into another list
        ArrayList < Integer > al1 = new ArrayList < Integer > (al);
        System.out.println (al1);
    }
}
