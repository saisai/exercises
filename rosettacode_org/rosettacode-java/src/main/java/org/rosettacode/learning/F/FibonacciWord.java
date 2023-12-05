package org.rosettacode.learning.F;

import java.util.HashMap;
import java.util.Map;

public class FibonacciWord {
    private String fWord0 = "";
    private String fWord1 = "";

    private String nextWord() {
        final String result;
        if("".equals(fWord1)) result = "1";
        else if("".equals(fWord0)) result = "0";
        else result = fWord1 + fWord0;

        fWord0 = fWord1;
        fWord1 = result;

        return result;
    }

    public static double entropy(final String source) {
        final int length = source.length();
        final Map<Character, Integer> counts = new HashMap<Character, Integer>();
        double result = 0.0;
        for(int i = 0; i < length; i++) {
            final  char c = source.charAt(i);
            if(counts.containsKey(c)) counts.put(c, counts.get(c) + 1);
            else counts.put(c, 1);
        }

        for(final int count : counts.values()) {
            final double propotion = (double) count/ length;
            result -= propotion * (Math.log(propotion) / Math.log(2));
        }
        return result;
    }

    public static void main(String[] args) {
        final FibonacciWord fWord = new FibonacciWord();
        for(int i = 0; i < 37; ) {
            final String word = fWord.nextWord();

            System.out.printf("%3d %10d %s %n", ++i, word.length(), entropy ( word ));
        }
    }
}
