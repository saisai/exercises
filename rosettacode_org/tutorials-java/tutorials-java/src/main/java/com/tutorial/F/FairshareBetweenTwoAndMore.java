package com.tutorial.F;

import org.w3c.dom.stylesheets.LinkStyle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FairshareBetweenTwoAndMore {
    private static List<Integer> thueMorseSequence(int terms, int base) {
        List<Integer> sequence = new ArrayList<Integer>();
        for(int i = 0; i < terms; i++) {
            int sum = 0;
            int n = i;
            while(n > 0) {
                // compute the digit sum
                sum +=  n % base;
                n /= base;
            }
            // Compute the digit sum module base.
            sequence.add(sum % base);
        }
        return sequence;
    }

    public static void main(String[] args) {
        for(int base : Arrays.asList(2, 3, 5, 22)) {
            System.out.printf("Base %d = %s%n", base, thueMorseSequence(25, base));
        }
    }
}
