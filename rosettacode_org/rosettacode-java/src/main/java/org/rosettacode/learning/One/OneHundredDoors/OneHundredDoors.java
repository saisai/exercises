package org.rosettacode.learning.One.OneHundredDoors;

import java.util.BitSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class OneHundredDoors {
    public void hundredDoorsBoolean() {
        boolean[] doors = new boolean[101];
        for(int i = 1; i < doors.length; i++) {
            for(int j = i ; j < doors.length; j += 1) {
                doors[j] = !doors[j];
            }
        }

        for(int i = 1; i < doors.length; i++) {
            if(doors[i]) {
                System.out.printf("Door %d is open.%n", i);
            }
        }
    }

    public void hundredDoorsBiset() {
        final int n = 100;
        BitSet a = new BitSet(n);
        for(int i = 1; i <= n; i++) {
            for(int j = i - 1; j < n; j+= i) {
                a.flip(j);
            }
        }
        a.stream().map(i -> i + 1).forEachOrdered(System.out::println);
    }

    public void hundredDoorsIntStream() {
        String openDoors = IntStream.rangeClosed(1, 100)
                .filter(i -> Math.pow((int) Math.sqrt(i), 2) == i)
                .mapToObj(Integer::toString)
                .collect(Collectors.joining(", "));
        System.out.printf("Open doors: %s%n", openDoors);
    }

    public static void main(String[] args) {
        OneHundredDoors obj = new OneHundredDoors();
//        obj.hundredDoorsBoolean();
//        obj.hundredDoorsBiset();
        obj.hundredDoorsIntStream();
    }
}
