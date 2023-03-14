package com.mycompany.slidingwindow;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FindAllAnagramsInAString {
    static List<Integer> findAnagrams(String s, String p) {
        int startIndex = 0;
        Map<Character, Integer> pMap = new HashMap<>(), sMap = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for(char c : p.toCharArray()) {
            pMap.put(c, 1 + pMap.getOrDefault(c, 0));
        }

        for(int i = 0; i < s.length(); i++) {
            sMap.put(s.charAt(i), 1 + sMap.getOrDefault(s.charAt(i), 0));

            if(i >= p.length() - 1) {
                if(sMap.equals(pMap)) {
                    res.add(startIndex);
                }

                // if current character is in sMap, remove it and re-update the map.
                if(sMap.containsKey(s.charAt(startIndex))) {
                    sMap.put(s.charAt(startIndex), sMap.get(s.charAt(startIndex)) - 1);
                    if(sMap.get(s.charAt(startIndex)) == 0) {
                        sMap.remove(s.charAt(startIndex));
                    }
                }
                startIndex += 1;
            }
        }
        return res;
    }

    public static void main(String... args) {
        String s = "cbaebabacd", p = "abc";
        System.out.println(findAnagrams(s, p));
    }
}
