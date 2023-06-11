package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class ex2 {

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(List.of(1, 2, 3, 4, 5, 4, 3, 2, 1));

        System.out.println(list);

        Predicate<Integer> isEven = i -> i % 2 == 0;

        list.removeIf(isEven);

        System.out.println(list);
    }
}
