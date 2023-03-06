package com.tutorial.A;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.*;

public class Anagrams {
    public static void main(String[] args) throws IOException {
        URL url = new URL("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt");
        InputStreamReader isr = new InputStreamReader(url.openStream());
        BufferedReader reader = new BufferedReader(isr);

        Map<String, Collection<String>> anagrams = new HashMap<String, Collection<String>>();
        String word;
        int count = 0;
        while((word = reader.readLine()) != null) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if(!anagrams.containsKey(key))
                anagrams.put(key, new ArrayList<String>());
            anagrams.get(key).add(word);
            count = Math.max(count, anagrams.get(key).size());
        }

        reader.close();

        for(Collection<String> ana : anagrams.values()) {
            if (ana.size() >= count) {
                System.out.println(ana);
            }
        }
    }
}
