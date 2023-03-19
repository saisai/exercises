package api.java.util.hashsets;

import dto.Customer;
import sun.util.resources.cldr.zh.CalendarData_zh_Hans_HK;

import java.util.HashSet;
import java.util.Set;

public class HashSetUserDefinedObjectExample {

    public static void main(String... args) {
        Set<Customer> customers = new HashSet<>();

        customers.add(new Customer(101, "Rajeev"));
        customers.add(new Customer(102, "Sachin"));
        customers.add(new Customer(103, "Chris"));

        /*
          HashSet will use the `equals()` & `hashCode()` implementations
          of the Customer class to check for duplicates and ignore them
        */
        customers.add(new Customer(101, "Rajeev"));

        System.out.println(customers);

    }
}
