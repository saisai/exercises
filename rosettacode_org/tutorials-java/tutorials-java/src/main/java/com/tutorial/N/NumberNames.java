package com.tutorial.N;

public class NumberNames {
    private static final String[] small = {
            "", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    private static final String[] tens = {
            "", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"};
    private static final String[] big = {
            "", "thousand", "million", "billion", "trillion",
            "quadrillion", "quintillion"};

    public static String int2Text(long number) {
        StringBuilder sb = new StringBuilder();
        if(number == 0) {
            return "Zero";
        }

        long num = -Math.abs(number);

        int unit = 1;
        while(true) {
            int rem100 = (int) -(num % 100);
            if(rem100 >= 20) {
                if(rem100 % 10 == 0) {
                    sb.insert(0, tens[rem100 / 10] + " ");
                } else {
                    sb.insert(0, tens[rem100 / 10] + "-" + small[rem100 % 10] + " ");
                }
            } else if (rem100 != 0) {
                sb.insert(0, small[rem100] + " ");
            }

            int hundreds = (int) -(num % 1000) / 100;
            if(hundreds != 0) {
                sb.insert(0, small[hundreds] + "hundred ");
            }

            num /= 1000;
            if(num == 0) {
                break;
            }

            int rem1000 = (int) -(num % 1000);
            if(rem1000 != 0) {
                sb.insert(0, big[unit] + " ");
            }
            unit++;
        }

        if(number < 0) {
            sb.insert(0, "negative");
        }

        return sb.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(int2Text(0));
        System.out.println(int2Text(10));
        System.out.println(int2Text(30));
        System.out.println(int2Text(47));
        System.out.println(int2Text(100));
        System.out.println(int2Text(999));
        System.out.println(int2Text(1000));
        System.out.println(int2Text(9999));
        System.out.println(int2Text(123_456));
        System.out.println(int2Text(900_000_001));
        System.out.println(int2Text(1_234_567_890));
        System.out.println(int2Text(-987_654_321));
        System.out.println(int2Text(Long.MAX_VALUE));
        System.out.println(int2Text(Long.MIN_VALUE));

        System.out.println("Recursive");
        System.out.println(NumberToWordsConverter.convert(1));
        System.out.println(NumberToWordsConverter.convert(90009));
    }

    public static class NumberToWordsConverter { // works upto 9999999

        final private  static String[] units = {"Zero","One","Two","Three","Four",
                "Five","Six","Seven","Eight","Nine","Ten",
                "Eleven","Twelve","Thirteen","Fourteen","Fifteen",
                "Sixteen","Seventeen","Eighteen","Nineteen"};
        final private static String[] tens = {"","","Twenty","Thirty","Forty","Fifty",
                "Sixty","Seventy","Eighty","Ninety"};

        public static String convert(Integer i) {
            //
            if( i < 20)  return units[i];
            if( i < 100) return tens[i/10] + ((i % 10 > 0)? " " + convert(i % 10):"");
            if( i < 1000) return units[i/100] + " Hundred" + ((i % 100 > 0)?" and " + convert(i % 100):"");
            if( i < 1000000) return convert(i / 1000) + " Thousand " + ((i % 1000 > 0)? " " + convert(i % 1000):"") ;
            return convert(i / 1000000) + " Million " + ((i % 1000000 > 0)? " " + convert(i % 1000000):"") ;
        }
    }
}
