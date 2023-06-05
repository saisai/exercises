package com.mycompany.leetcode.medium.SearchSuggestionsSystem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SearchSuggestionsSystemChappy1 {

    static List<List<String>> ans;

    private static int binarySearchFirstOccurrence(String[] products, int l, int h, int i, char target) {
        int low = l;
        int high = h;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (products[mid].length() <= i) {
                low = mid + 1;
            } else {
                if (products[mid].charAt(i) < target) low = mid + 1;
                else high = mid;
            }
        }
        if (products[low].length() <= i || products[low].charAt(i) != target) return -1;
        return low;
    }

    private static int binarySearchLastOccurrence(String[] products, int l, int h, int i, char target) {
        int low = l;
        int high = h;
        while (low < high) {
            int mid = low + (high - low + 1) / 2;
            if (products[mid].length() <= i) {
                low = mid;
            } else {
                if (products[mid].charAt(i) > target) high = mid - 1;
                else low = mid;
            }
        }
        if (products[low].length() <= i || products[low].charAt(i) != target) return -1;
        return low;
    }

    static List<List<String>> suggestedProducts(String[] products, String searchWord) {
        ans = new ArrayList<>();
        char[] array = searchWord.toCharArray();
        Arrays.sort(products);
        int low = 0;
        int high = products.length - 1;
        for (int i = 0; i < array.length; i++) {
            if (low > high) {
                ans.add(new ArrayList<>());
                continue;
            }
            char target = array[i];
            int idx = binarySearchFirstOccurrence(products, low, high, i, target);
            if (idx == -1) {
                ans.add(new ArrayList<>());
                low = high + 1;
                continue;
            }
            low = idx;
            high = binarySearchLastOccurrence(products, low, high, i, target);
            List<String> res = new ArrayList<>();
            for (int j = 0; j < 3 && j + low <= high; j++) res.add(products[j + low]);
            ans.add(res);
        }
        return ans;
    }

    public static void main(String[] args) {
        String[] products = {"mobile","mouse","moneypot","monitor","mousepad"};
        String searchWord = "mouse";

        List<List<String>> listOfLists= suggestedProducts(products, searchWord);
        listOfLists.forEach(innerList -> {
            String line = String.join(", ", innerList);
            System.out.println(line);
        });

    }
}
