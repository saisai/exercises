package com.tutorial.W.WalkADirectory;

import java.io.File;
import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;

public class Recursively {

    static class RecursivelyJava1Plus4 {

        public void mainEntry() {
            walkin(new File("D:\\data"));
        }

        private void walkin(File dir) {
            String pattern = ".mp3";

            File[] listFile = dir.listFiles();
            if(listFile != null) {
                for(int i = 0; i < listFile.length; i++) {
                    if(listFile[i].isDirectory()) {
                        walkin(listFile[i]);
                    } else {
                        if(listFile[i].getName().endsWith(pattern)) {
                            System.out.println(listFile[i].getPath());
                        }
                    }
                }
            }
        }
    }

    static class WalkTreeJava7Plus {
        void mainEntry()  {
            try {
                Path start = FileSystems.getDefault().getPath("D:\\data");
                Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
                    @Override
                    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                        if (file.toString().endsWith(".mp3")) {
                            System.out.println(file);
                        }
                        return FileVisitResult.CONTINUE;
                    }

                });
            } catch(IOException e) {
                System.out.println("ERROR : " + e.getMessage());
            }
        }
    }

    static class WalkTreeJava8Plus {
        void mainEntry() {
            try {
                Path start = FileSystems.getDefault().getPath("D:\\data");
                Files.walk(start)
                        .filter(path -> path.toFile().isFile())
                        .filter(path -> path.toString().endsWith(".mp3"))
                        .forEach(System.out::println);
            } catch(IOException e) {
                System.out.println("ERROR :" + e.getMessage());
            }
        }
    }
    public static void main(String... args)  {
        new RecursivelyJava1Plus4().mainEntry();
        new WalkTreeJava7Plus().mainEntry();
        new WalkTreeJava8Plus().mainEntry();
    }
}
