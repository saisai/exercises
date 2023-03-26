package com.tutorial.R;

import com.tutorial.Utils;

import java.io.*;
import java.lang.reflect.Method;
import java.util.Arrays;

public class ReadASpecificLineFromAFile {

    private static Method normalizedList() throws NoSuchMethodException {
        Method method = Utils.class.getDeclaredMethod("normalizedList", File.class);
        method.setAccessible(true);
        return method;
    }
    public static void main(String... args) throws Exception {
        String fileName = new Utils().getFilename("unixdict.txt");
        File f = new File(fileName);
        if(!f.isFile() || !f.canRead()) {
            throw new IOException("can't read " + fileName);
        }

        System.out.println(f.getPath());
        System.out.println(f.getName());
        System.out.println(f.getParent());
        System.out.println(f.getParentFile());
        System.out.println(f.getAbsolutePath());
        System.out.println("can read " + f.canRead());
        System.out.println("can read " + f.canWrite());
        System.out.println("exists " + f.exists());
        System.out.println("Is directory " + f.isDirectory());
        System.out.println("Last Modified " + f.lastModified());
        System.out.println("Length " + f.length());
        //System.out.println("normalizedList " + f.normalizedList());
        //System.out.println("normalizedList " + f.normalizedList());
        System.out.println("list " + Arrays.toString(f.list()) );
        System.out.println("getTotalSpace " + f.getTotalSpace());
        System.out.println("getFreeSpace " + f.getFreeSpace());
        System.out.println("getUsableSpace " + f.getUsableSpace());
        System.out.println("toPath " + f.toPath());



        BufferedReader br = new BufferedReader(new FileReader(f));
        try(LineNumberReader lnr = new LineNumberReader(br)) {
            String line = null;
            int lnum = 0;
            while((line = lnr.readLine()) != null && (lnum = lnr.getLineNumber()) < 7){

            }
            switch (lnum) {
                case 0:
                    System.out.println("the file has zero length");
                    break;
                case 7:
                    boolean empty = "".equals(line);
                    System.out.println("line 7:" + (empty ? "empty" : line));
                    break;
                default:
                    System.out.println("the file has only " + lnum + " line(s)");
            }
        }
    }
}
