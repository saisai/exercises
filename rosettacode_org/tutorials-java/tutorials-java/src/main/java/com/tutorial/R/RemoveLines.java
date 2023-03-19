package com.tutorial.R;

import sun.misc.ClassLoaderUtil;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Objects;

public class RemoveLines {

    static String fileName;

    RemoveLines() {
        fileName = getFilename1();
    }

    String getFilename1() {
        String filePath = Objects.requireNonNull(getClass().getClassLoader().getResource("foobar.txt")).getPath();
        System.out.println("file path " + filePath);
        return filePath;
    }


    public static void main(String... args) {
        RemoveLines now = new RemoveLines();
        System.out.println("getfilename " + now.getFilename1());
        int startline = 1;
        int numlines = 2;
        System.out.println(fileName);
        now.delete(fileName, startline, numlines);
    }

    void delete(String fileName, int startline, int numlines) {
        try{

            BufferedReader br = new BufferedReader(new FileReader(fileName));

            // String buffer to store contents of the file
            StringBuffer sb = new StringBuffer("");

            // keep track of the line number
            int linenumber = 1;
            String line;

            while((line= br.readLine()) != null) {
                System.out.println(line);
                // store each valid line in the string buffer
                if(linenumber<startline||linenumber>= startline + numlines)
                    sb.append(line+"\n");
                linenumber++;
            }
            if(startline + numlines > linenumber)
                System.out.println("End of file reaced");
            br.close();

            FileWriter fw = new FileWriter(new File(fileName));
            // Write entire string buffer into the file
            fw.write(sb.toString());
            fw.close();
        } catch (Exception e) {
            System.out.println("Something went horribly wrong:  " + e.getMessage());
        }
    }
}
