package com.mycompany.docsoraclecom.essential.io;

import utils.FileUtils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URISyntaxException;

public class CopyBytes {

    public static void main(String[] args) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;

        try {

            FileUtils fileUtils = new FileUtils();
            in = new FileInputStream(fileUtils.getResourceFile("xanadu.txt"));
            out = new FileOutputStream(fileUtils.getResourceFile("outagain.txt"));
            int c;
            while(( c = in.read()) != -1) {
                System.out.println(c);
                out.write((char)c);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            if(in  != null) {
                in.close();
            }
            if(out != null) {
                out.close();
            }
        }
    }
}
