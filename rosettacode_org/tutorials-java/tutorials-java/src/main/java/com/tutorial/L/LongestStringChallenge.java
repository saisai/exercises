package com.tutorial.L;

import com.tutorial.Utils;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class LongestStringChallenge {

    public static boolean longer(String a, String b) {
        try {
            String dummy = a.substring(b.length());
        } catch (StringIndexOutOfBoundsException e) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Path currentRelativePath = Paths.get("");
        String s = currentRelativePath.toAbsolutePath().toString();
        System.out.println("Current absolute path is: " + s);
        System.out.print(new File("").getAbsoluteFile());
        URL location = LongestStringChallenge.class.getProtectionDomain().getCodeSource().getLocation();
        System.out.println(location.getFile());
        String userDirectory = Paths.get("src/main/java/com/tutorial/L")
                .toAbsolutePath()
                .toString();
        System.out.println(userDirectory);
        String fileName = userDirectory.concat("\\hello.txt");

        System.out.println("file Name " + fileName);
        System.out.println("file Name " + Utils.fileExists(fileName));
        String lines = "", longest = "";
        //try(Scanner sc = new Scanner(new File("hello.txt"))) {
        try(Scanner sc = new Scanner(new File(fileName))) {
            while(sc.hasNext()) {
                String line = sc.nextLine();
//                System.out.println("f " + line);
                if(longer(longest, line))
                    lines = longest = line;
                else if (!longer(line, longest))
                    lines = lines.concat("\n").concat(line);
            }
        }
        System.out.println(lines);
    }
}
