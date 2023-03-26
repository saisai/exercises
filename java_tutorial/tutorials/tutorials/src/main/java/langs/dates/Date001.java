package langs.dates;

import java.util.Date;

public class Date001 {
    public static void main(String... args) {
        Date date = new Date();
        System.out.println(date);

        Date d1 = new Date(2020, 2, 20);
        System.out.println(d1);
        System.out.println();
        System.out.println(d1.getYear());
        System.out.println(d1.getDate());
        System.out.println();
    }
}
