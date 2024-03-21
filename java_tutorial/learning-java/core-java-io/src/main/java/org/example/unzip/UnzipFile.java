package org.example.unzip;

import java.io.*;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
public class UnzipFile {
    public static void main(final String[] args) throws IOException, URISyntaxException {
//        final String fileZip = "src/main/resources/unzipTest/compressed.zip";
        final File destDir = new File("src/main/resources/unzipTestt");

        ClassLoader classloader = Thread.currentThread().getContextClassLoader();
        InputStream is = classloader.getResourceAsStream("unzipTest/compressed.zip");

        final byte[] buffer = new byte[1024];
        final ZipInputStream zis = new ZipInputStream(is);


        ZipEntry zipEntry = zis.getNextEntry();
        System.out.println("zipEntry " + zipEntry);
        while (zipEntry != null) {
            final File newFile = newFile(destDir, zipEntry);
            System.out.println("newFile " + newFile);
            if (zipEntry.isDirectory()) {
                if (!newFile.isDirectory() && !newFile.mkdirs()) {
                    throw new IOException("Failed to create directory " + newFile);
                }
            } else {
                File parent = newFile.getParentFile();
                if (!parent.isDirectory() && !parent.mkdirs()) {
                    throw new IOException("Failed to create directory " + parent);
                }

                final FileOutputStream fos = new FileOutputStream(newFile);
                System.out.println("fos " + fos);
                int len;
                while ((len = zis.read(buffer)) > 0) {
                    fos.write(buffer, 0, len);
                }
                fos.close();
            }
            zipEntry = zis.getNextEntry();
        }
        zis.closeEntry();
        zis.close();
    }

    /**
     * @see https://snyk.io/research/zip-slip-vulnerability
     */
    public static File newFile(File destinationDir, ZipEntry zipEntry) throws IOException {
        File destFile = new File(destinationDir, zipEntry.getName());

        String destDirPath = destinationDir.getCanonicalPath();
        String destFilePath = destFile.getCanonicalPath();

        if (!destFilePath.startsWith(destDirPath + File.separator)) {
            throw new IOException("Entry is outside of the target dir: " + zipEntry.getName());
        }

        return destFile;
    }
}
