package org.rosettacode.learning.D.DigitalRoot;

import java.math.BigInteger;

public class DigitalRoot {
    public static int[] calcDigitalRoot(String number, int base) {
        BigInteger bi = new BigInteger(number, base);
        int additivePersistence = 0;
        if(bi.signum() < 0)
            bi = bi.negate();
        BigInteger biBase = BigInteger.valueOf(base);
        while(bi.compareTo(biBase) >= 0) {
            number = bi.toString(base);
            bi = BigInteger.ZERO;
            for(int i = 0; i < number.length(); i++)
                bi = bi.add(new BigInteger(number.substring(i, i + 1), base));
            additivePersistence++;
        }
        return new int[] {additivePersistence, bi.intValue()};
    }

    public static void main(String[] args) {
        for(String arg : args) {
            int[] results = calcDigitalRoot(arg, 10);
            System.out.println(arg + " has additive persitence " + results[0] + " and digital root of " + results[1]);
        }
    }
}

// C:\Users\wan>D:\programs\jdks\17\bin\java.exe "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.3.2\lib\idea_rt.jar=59540:C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.3.2\bin" -Dfile.encoding=UTF-8 -classpath D:\exercises\rosettacode_org\rosettacode-java\target\classes;C:\Users\wan\.m2\repository\com\google\code\gson\gson\2.10.1\gson-2.10.1.jar org.rosettacode.learning.D.DigitalRoot.DigitalRoot 30405