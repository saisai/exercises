package com.mycompany.goodrich6thedition.ch07;


public class SortingPositionalList {
    public static void insertionSort(PositionalList<Integer> list) {
        Position<Integer> marker = list.first();
        while(marker != list.last()) {
            Position<Integer> pivot = list.after(marker);
            int value = pivot.getElement();
            if(value > marker.getElement())
                marker = pivot;
            else {
                Position<Integer> walk = marker;
                while(walk != list.first() && list.before(walk).getElement() > value)
                    walk = list.before(walk);
                list.remove(pivot);
                list.addBefore(walk, value);
            }
        }

    }

    public static void main(String[] args) {
        LinkedPositionalList<Integer> list = new LinkedPositionalList<>();
        Position<Integer> first = list.addFirst(1);
        Position<Integer> second = list.addAfter(first, 4);
        list.addAfter(second, 0);
        list.addBefore(first, 20);
        insertionSort(list);
        for(Integer thing : list) {
            System.out.println(thing);
        }

    }
}
