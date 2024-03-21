package org.example.zip;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class ZipFile {
    public static void main(final String[] args) throws IOException, URISyntaxException {
//        final String sourceFile = "src/main/resources/zipTest/test1.txt";
        final FileOutputStream fos = new FileOutputStream("src/main/resources/compressed.zip");
        final ZipOutputStream zipOut = new ZipOutputStream(fos);
        URL zipUrl = ZipFile.class.getClassLoader().getResource("zipTest/test1.txt");
        File zipFile = new File(zipUrl.toURI());
        final File fileToZip = zipFile;
        final FileInputStream fis = new FileInputStream(fileToZip);
        final ZipEntry zipEntry = new ZipEntry(fileToZip.getName());
        zipOut.putNextEntry(zipEntry);
        final byte[] bytes = new byte[1024];
        int length;
        while ((length = fis.read(bytes)) >= 0) {
            zipOut.write(bytes, 0, length);
        }
        zipOut.close();
        fis.close();
        fos.close();
    }
}