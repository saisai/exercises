package com.companyname.packagename.W;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class WordCount {

    public static String readResource() throws UnsupportedEncodingException, IOException {

        InputStream is = WordCount.class.getClassLoader().getResourceAsStream("135-0.txt");
        InputStreamReader isr = new InputStreamReader(is, "UTF-8");
        BufferedReader file = new BufferedReader(isr);

        StringBuilder builder = new StringBuilder();
        String line = null; // line read from file
        while ((line = file.readLine()) != null) {
            //System.out.println(line);
            builder.append(line).append("\n");
        }

        file.close(); isr.close(); is.close();

        return builder.toString();

    }
    public static void main(String... args) throws IOException {

        //Path path = Paths.get("135-0.txt");
//        Path path = Paths.get(readResource().toString());
//
//        byte[] bytes = Files.readAllBytes(path);
        String text = new String(readResource());
        text = text.toLowerCase();

        Pattern r = Pattern.compile("\\p{javaLowerCase}+");
        Matcher matcher = r.matcher(text);
        Map<String, Integer> freq = new HashMap<>();
        while(matcher.find()) {
            String word = matcher.group();
            Integer current = freq.getOrDefault(word, 0);
            freq.put(word, current + 1);
        }
        List<Map.Entry<String, Integer>> entries = freq.entrySet()
                .stream()
                .sorted((i1, i2) -> Integer.compare(i2.getValue(), i1.getValue()))
                .limit(10)
                .collect(Collectors.toList());

        System.out.println("Rank word Frequency");
        System.out.println("==== ==== =========");
        int rank = 1;
        for(Map.Entry<String, Integer> entry : entries) {
            String word = entry.getKey();
            Integer count = entry.getValue();
            System.out.printf("%2d    %-4s    %5d\n", rank++, word, count);
        }

    }
}
