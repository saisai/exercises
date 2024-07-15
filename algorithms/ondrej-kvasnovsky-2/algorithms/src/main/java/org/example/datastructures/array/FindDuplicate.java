package org.example.datastructures.array;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FindDuplicate {
    public static void main(String[] args) {
        Integer[] array = new Integer[]{1, 2, 3, 4, 5, 1};

        List<Integer> ints = Arrays.asList(array);
        Set<Integer> unique = new HashSet<>(ints);

        boolean containsDuplicate = ints.size () != unique.size();
        System.out.println(containsDuplicate);
    }
}

 // https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/array/find-duplicates
