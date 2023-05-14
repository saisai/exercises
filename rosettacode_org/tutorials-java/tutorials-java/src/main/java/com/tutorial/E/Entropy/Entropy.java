package com.tutorial.E.Entropy;

import java.util.HashMap;
import java.util.Map;

public class Entropy {

    @SuppressWarnings("boxing")
    public static double getShannonEntropy(String s) {
        int n = 0;
        Map<Character, Integer> occ = new HashMap<>();
        for(int c_ = 0; c_ < s.length(); ++c_) {
            char cx = s.charAt(c_);
            if(occ.containsKey(cx)) {
                occ.put(cx, occ.get(cx) + 1);
            } else {
                occ.put(cx, 1);
            }
            ++n;
        }

        double e = 0.0;
        for(Map.Entry<Character, Integer> entry : occ.entrySet()) {
            char cx = entry.getKey();
            double p = (double) entry.getValue() / n;
            e += p * log2(p);
        }
        return -e;
    }

    private static double log2(double a) {
        return Math.log(a) / Math.log(2);
    }

    public static void main(String[] args) {
        String[] sstr = {
                "1223334444",
                "1223334444555555555",
                "122333",
                "1227774444",
                "aaBBcccDDDD",
                "1234567890abcdefghijklmnopqrstuvwxyz",
                "Rosetta Code",
        };

        for(String ss : sstr) {
            double entropy = getShannonEntropy(ss);
            System.out.printf("Shannon entryopy of %40s : %.12f%n", "\"" + ss + "\"", entropy);
        }
    }
}
