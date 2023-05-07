package com.tutorial;

import java.io.File;
import java.nio.file.Paths;
import java.util.Objects;

public class Utils {

    public static String getDirectory(String directory) {
        String userDirectory = Paths.get(directory)
                .toAbsolutePath()
                .toString();
        return userDirectory;
    }

    public static boolean fileExists(String filePathString) {
        File f = new File(filePathString);
        if(f.exists() || !f.isDirectory()) {
            // do something
            return true;
        }
        return false;
    }

     public String getFilename(String fileName) {
        String filePath = Objects.requireNonNull(getClass().getClassLoader().getResource(fileName)).getPath();
        System.out.println("file path " + fileName);
        return filePath;
    }

    public static String getFilenameAndPath(String filePathAndFileName) {
        File file = new File(filePathAndFileName);
        System.out.println("exists " + file.exists());
        String filePath = file.getAbsolutePath();
        return filePath;
    }

}
