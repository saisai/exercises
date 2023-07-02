package com.mycompany.docsoraclecom.collections.list;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Deal {
    public static void main(String[] args) {
//        if(args.length < 2) {
//            System.out.println("Usage: Deal hands cards");
//            return;
//
//        }
        String[] testArgs = {"4", "5"};
        int numHands = Integer.parseInt(testArgs[0]);
        int cardsPerHand = Integer.parseInt(testArgs[1]);

        // Make a nomral 52-card deck.
        String[] suit = new String[] {
                "spades", "hearts",
                "diamons", "clubs"
        };

        String[] rank = new String[] {
                "ace", "2", "3", "4",
                "5", "6", "7", "8", "9", "10",
                "jack", "queen", "king"
        };

        List<String> deck = new ArrayList<String>();

        for(int i = 0; i < suit.length; i++) {
            for(int j = 0; j < rank.length; j++) {
                deck.add(rank[j] + " of " + suit[i]);
            }
        }

        // Shuffle the deck
        Collections.shuffle(deck);

        if(numHands * cardsPerHand > deck.size()) {
            System.out.println("Not enough cards");
            return;
        }

        for(int i = 0; i < numHands; i++) {
            System.out.println(dealHand(deck, cardsPerHand));
        }
    }

    static <E> List<E> dealHand(List<E> deck, int n) {
        int deckSize = deck.size();
        List<E> handView = deck.subList(deckSize - n, deckSize);
        List<E> hand = new ArrayList<E>(handView);
        handView.clear();
        return hand;
    }
}
