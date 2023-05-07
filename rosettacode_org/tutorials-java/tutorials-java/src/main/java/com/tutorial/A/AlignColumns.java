package com.tutorial.A;


import com.tutorial.Utils;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class AlignColumns {

    private List<String[]> words = new ArrayList<>();
    private int columns = 0;
    private List<Integer> columnWidths = new ArrayList<>();

    public AlignColumns(String s) {
        String[] lines = s.split("\\n");
        for(String line : lines) {
            processInputLine(line);
        }
    }

    private void processInputLine(String line) {
        String[] lineWords = line.split("\\$");
        words.add(lineWords);
        columns = Math.max(columns, lineWords.length);
        for(int i = 0; i < lineWords.length; i++) {
            String word = lineWords[i];
            if(i >= columnWidths.size()) {
                columnWidths.add(word.length());
            } else {
                columnWidths.set(i, Math.max(columnWidths.get(i), word.length()));
            }
        }
    }

    interface AlignFunction {
        String align(String s, int length);
    }

    private String align(AlignFunction a) {
        StringBuilder result = new StringBuilder();
        for(String[] linewords : words) {
            for(int i = 0; i < linewords.length; i++) {
                String word = linewords[i];
                if(i == 0) {
                    result.append("|");
                }
                result.append(a.align(word, columnWidths.get(i)) + "|");
            }
            result.append("\n");
        }
        return result.toString();
    }

    public String alignLeft() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.rightPad(s, length);
            }
        });
    }

    public String alignRight() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.leftPad(s, length);
            }
        });
    }

    public String alignCenter() {
        return align(new AlignFunction() {
            @Override
            public String align(String s, int length) {
                return StringUtils.center(s, length);
            }
        });
    }

    public static void main(String[] args) throws IOException {
        if(args.length < 1) {
            System.out.println("Usage: ColumnAligner file [left|right|center]");
            return;
        }

        String filePath = Utils.getFilenameAndPath(args[0]);
        String alignment = "left";
        if(args.length >= 2) {
            alignment = args[1];
        }

//        File file = new File("src/main/resources/string.txt");
//        System.out.println("exists " + file.exists());
//        String filePath = file.getAbsolutePath();

//        String filePath = Utils.getFilenameAndPath("string.txt");
//        String s = Files.readAllLines(Paths.get(filePath), StandardCharsets.UTF_8).toString();
//        System.out.println(s);
        AlignColumns ac = new AlignColumns(Files.readAllLines(Paths.get(filePath), StandardCharsets.UTF_8).toString());
        switch (alignment) {
            case "left":
                System.out.print(ac.alignLeft());
                break;
            case "right":
                System.out.print(ac.alignRight());
                break;
            case "center":
                System.out.print(ac.alignCenter());
                break;
            default:
                System.err.println(String.format("Error! Unknown alignment: '%s'", alignment));
                break;
        }
    }
}
