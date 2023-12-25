package com.mycompany.leetcode.grind75.week5.AccountsMerge;

import java.util.*;
import java.util.stream.Collectors;

public class AccountsMergeAlexander {
    public List<List<String>> accountsMerge(List<List<String>> acts) {
        Map<String, String> owner = new HashMap<>();
        Map<String, String> parents = new HashMap<>();
        Map<String, TreeSet<String>> unions = new HashMap<>();
        for(List<String> a : acts) {
            for(int i = 1; i < a.size(); i++) {
                parents.put(a.get(i), a.get(i));
                owner.put(a.get(i), a.get(0));
            }
        }

        owner.forEach((K, V) -> {
            System.out.println(K + "=>" + V);
        });


        for(List<String> a : acts) {
            String p = find(a.get(1), parents);
            for(int i = 2; i < a.size(); i++) {
                parents.put(find(a.get(i), parents), p);
            }
        }

        for(List<String> a : acts) {
            String p = find(a.get(1), parents);
            if(!unions.containsKey(p)) unions.put(p, new TreeSet<>());
            for(int i = 1; i < a.size(); i++)
                unions.get(p).add(a.get(i));
        }

        List<List<String>> res = new ArrayList<>();
        for(String p : unions.keySet()) {
            List<String> emails = new ArrayList<>(unions.get(p));
            emails.add(0, owner.get(p));
            res.add(emails);
        }
        return res;
    }

    private String find(String s, Map<String, String> p) {
        return p.get(s) == s ? s : find(p.get(s), p);
    }

    public static void main(String[] args) {
        String[][] accounts = {{"John","johnsmith@mail.com","john_newyork@mail.com"},
                {"John","johnsmith@mail.com","john00@mail.com"},{"Mary","mary@mail.com"},{"John","johnnybravo@mail.com"}};

        List<List<String>> accounts2 = Arrays.stream(accounts).map(Arrays::asList).collect(Collectors.toList());
        AccountsMergeAlexander obj = new AccountsMergeAlexander();
        List<List<String>> results = obj.accountsMerge(accounts2);

        results.forEach(lst -> {
            System.out.println(lst);
        });
    }
}


// https://stackoverflow.com/questions/16206551/casting-2d-array-to-list-of-lists-in-java
// https://stackoverflow.com/questions/29888539/java-8-map-lambda-expression
// https://stackoverflow.com/questions/40511450/printing-hashmap-of-hashmaps-map-entry-or-java8