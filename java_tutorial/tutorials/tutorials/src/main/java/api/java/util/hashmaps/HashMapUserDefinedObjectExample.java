package api.java.util.hashmaps;

import dto.Employee;

import java.util.HashMap;
import java.util.Map;

public class HashMapUserDefinedObjectExample {
    public static void main(String... args) {
        Map<Integer, Employee> employeesMap = new HashMap<>();

        employeesMap.put(1001, new Employee(1001, "Rajeev", "Bengaluru"));

        employeesMap.put(1002, new Employee(1002, "David", "New York"));
        employeesMap.put(1003, new Employee(1003, "Jack", "Paris"));

        System.out.println(employeesMap);
    }
}
