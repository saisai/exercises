package com.tutorial.I;

import com.tutorial.Utils;

import java.io.BufferedReader;
import java.io.FileReader;

public class IbeforeE {

    boolean isPlausibleRule(String filename) {
        int truecount = 0, falsecount = 0;
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            String word;
            while((word=br.readLine()) != null) {
                //System.out.println("test " + word);
                if(isPlausibleWord(word)) {
                    truecount++;
                } else if (isOppPlausibleWord(word)) {
                    falsecount++;
                }
            }
            br.close();
        } catch (Exception e) {
            System.out.println("Something went wrong :" + e.getMessage());
        }
        System.out.println("Plausible count: " + truecount);
        System.out.println("Implausible count: "+ falsecount);
        if(truecount > 2 * falsecount)
            return true;
        return false;
    }

    boolean isPlausibleWord(String word) {
        if(!word.contains("c") && word.contains("ie"))
            return true;
        else if(word.contains("cei"))
            return true;
        return false;
    }

    boolean isOppPlausibleWord(String word){
        if(!word.contains("c") && word.contains("ei"))
            return true;
        else if(word.contains("cie"))
            return true;
        return false;
    }

    public static void main(String... args) {
        IbeforeE now = new IbeforeE();
        String wordlist = new Utils().getFilename("unixdict.txt");
        if(now.isPlausibleRule(wordlist))
            System.out.println("Rule is plausible.");
        else
            System.out.println("Rule is not plausible.");
    }
}
