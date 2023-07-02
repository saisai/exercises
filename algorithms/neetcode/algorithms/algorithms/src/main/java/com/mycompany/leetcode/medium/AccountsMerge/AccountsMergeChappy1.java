package com.mycompany.leetcode.medium.AccountsMerge;

import java.util.*;
import java.util.stream.Collectors;

public class AccountsMergeChappy1 {
    static class P {
        Map<String, Integer> emails = new HashMap<>();
        List<List<String>> groups = new ArrayList<>();

        void process (List<String> list) {
            Integer key = null;
            for(int i = 1; i < list.size(); i++) {
                String email = list.get(i);
                Integer existing = emails.get(email);
                if(existing != null) {
                    if(key == null) {
                        key = existing;
                    } else if (!key.equals(existing)) {
                        key = merge(existing, key);
                    }
                }
            }
            List<String> group;
            if(key == null) {
                key = groups.size();
                groups.add(group = new ArrayList<>());
            } else {
                group = groups.get(key);
            }

            for(int i = 1; i < list.size(); i++) {
                String email = list.get(i);
                if(emails.put(email, key) == null) {
                    group.add(email);
                }
            }
        }

        Integer merge(Integer key1, Integer key2) {
            List<String> gr1 = groups.get(key1);
            List<String> gr2 =groups.get(key2);

            if(gr1.size() > gr2.size()) {
                return merge(key2, key1);
            }
            for(String email : gr1) {
                emails.put(email, key2);
            }

            gr2.addAll(gr1);
            groups.set(key1, null);
            return key2;
        }
    }

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, P> map = new HashMap<>();
        for(List<String> list : accounts) {
            String name = list.get(0);
            map.computeIfAbsent(name, k -> new P()).process(list);
        }

        List<List<String>> result= new ArrayList<>();
        for(Map.Entry<String, P> entry : map.entrySet()) {
            for(List<String> group : entry.getValue().groups) {
                if(group != null) {
                    Collections.sort(group);
                    List<String> r = new ArrayList<String>(group.size() + 1);
                    r.add(entry.getKey());
                    r.addAll(group);
                    result.add(r);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String[][] accounts = {{"Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"}, {"Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"},
                {"Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"},
        {"Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"},{"Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"}};
        List<List<String>> list = Arrays.stream(accounts)
                .map(Arrays::asList)
                .collect(Collectors.toList());
        AccountsMergeChappy1 obj = new AccountsMergeChappy1();
        obj.accountsMerge(list).forEach(e -> System.out.println(e));

//        String s = "0 ";
//        int i = Integer.parseInt(s);
//        System.out.println(i);
    }
}

// https://stackoverflow.com/questions/11447780/convert-two-dimensional-array-to-list-in-java
// https://leetcode.com/problems/accounts-merge/solutions/3440606/solution/
// https://leetcode.com/problems/accounts-merge/solutions/1602173/python-simple-dfs-explained/
