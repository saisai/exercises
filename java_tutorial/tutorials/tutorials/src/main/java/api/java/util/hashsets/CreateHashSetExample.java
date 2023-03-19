package api.java.util.hashsets;

import java.util.HashSet;
import java.util.Set;

public class CreateHashSetExample {

    public static void main(String... args) {
        // create a HashSet
        Set<String> daysOfWeek = new HashSet<>();

        // adding new elements to the hashSet
        daysOfWeek.add("Monday");
        daysOfWeek.add("Tuesday");
        daysOfWeek.add("Wednesday");
        daysOfWeek.add("Thursday");
        daysOfWeek.add("Friday");
        daysOfWeek.add("Saturday");
        daysOfWeek.add("Sunday");

        // Adding duplicate elements will be ignored
        daysOfWeek.add("Monday");

        System.out.println(daysOfWeek);
    }
}
