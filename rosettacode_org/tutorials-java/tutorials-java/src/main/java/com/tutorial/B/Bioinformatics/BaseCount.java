package com.tutorial.B.Bioinformatics;

import java.util.HashMap;
import java.util.Map;

public class BaseCount {

    public static class Sequence {
        private final String seq;
        public Sequence(String sq) {
            this.seq = sq;
        }

        public void prettyPrint() {
            System.out.println("Sequence: ");
            int i = 0;
            for(; i < seq.length() - 50; i += 50) {
                System.out.printf("%5s : %s\n", i + 50, seq.substring(i, i + 50));
            }
            System.out.printf("%5s : %s\n", seq.length(), seq.substring(i));
        }

        public void displayCount() {
            Map<Character, Integer> counter = new HashMap<>();
            for(int i = 0; i < seq.length(); ++i) {
                counter.merge(seq.charAt(i), 1, Integer::sum);
            }

            System.out.println("Base vs. Count:");
            counter.forEach(
                    (key, value) -> System.out.printf("%5s : %s\n", key, value));
            System.out.printf("%5s : %s\n", "SUM", seq.length());
        }

        public void runSequence() {
            this.prettyPrint();
            this.displayCount();
        }
    }

    public static void main(String[] args) {
        Sequence gene = new Sequence("CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATGCTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATTCTGCTTATAACACTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATATTTAATTTTTCTATATAGCGATCTGTATTTAAGCAATTCATTTAGGTTATCGCCGCGATGCTCGGTTCGGACCGCCAAGCATCTGGCTCCACTGCTAGTGTCCTAAATTTGAATGGCAAACACAAATAAGATTTAGCAATTCGTGTAGACGACCGGGGACTTGCATGATGGGAGCAGCTTTGTTAAACTACGAACGTAAT");
        gene.runSequence();
    }
}
