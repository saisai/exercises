package com.zetcode.app.string;

import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.List;

public class StringBlank {

    public static void main(String[] args) {
        List<String > data = new ArrayList<>();
        data.add("sky");
        data.add("\n\n");
        data.add(" ");
        data.add("blue");
        data.add("\t\t");
        data.add("");
        data.add("sky");

        for(int i = 0; i < data.size(); i++) {
            String e = data.get(i);
            if (StringUtils.isBlank(e)) {
                System.out.printf("element with index %d is blank%n", i);
            } else {

                System.out.println(data.get(i));
            }
        }
    }
}
