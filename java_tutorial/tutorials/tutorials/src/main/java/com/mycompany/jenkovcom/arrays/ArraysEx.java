package com.mycompany.jenkovcom.arrays;

import java.util.Arrays;
import java.util.Comparator;

import static java.lang.System.out;

class Employee {
    public String name;
    public int employeeId;

    public Employee(String name, int employeeId) {
        this.name = name;
        this.employeeId = employeeId;
    }

    public String toString() {
        return this.name;
    }
}
public class ArraysEx {

    // Converting Arrays to Strings With Arrays.toString()
    static void ConvertingArraysToString() {
        int[] ints = new int[10];
        for(int i = 0; i < ints.length; i++) {
            ints[i] = 10 - i;
        }

        out.println(java.util.Arrays.toString(ints));
    }

    // Sorting Arrays
    static void SortingArrays() {
        int[]   ints = new int[10];

        for(int i=0; i < ints.length; i++){
            ints[i] = 10 - i;
        }
        out.println(java.util.Arrays.toString(ints));

        java.util.Arrays.sort(ints);

        out.println(java.util.Arrays.toString(ints));
    }

    // Sorting Arrays of Objects
    static void SortingObjects() {
        Employee[] employeeArray = new Employee[3];

        employeeArray[0] = new Employee("Xander", 1);
        employeeArray[1] = new Employee("John"  , 3);
        employeeArray[2] = new Employee("Anna"  , 2);

        // sort by name
        java.util.Arrays.sort(employeeArray, new Comparator<Employee>() {
            @Override
            public int compare(Employee o1, Employee o2) {
                return o1.name.compareTo(o2.name);
            }
        });

        /*
        Let us now see how it looks to sort the Employee objects by their employee id instead. Here is the example
        from before, with a modified implementation of the compare() method of the anonymous implementation of the Comparator interface:
         */
        // sort by id
        java.util.Arrays.sort(employeeArray, new Comparator<Employee>() {
            @Override
            public int compare(Employee e1, Employee e2) {
                return e1.employeeId - e2.employeeId;
            }
        });

        /*
        To compare the Employee objects in the array first by their name, and if that is the same,
        then by their employee id, the compare() implementation would look like this:
         */
        java.util.Arrays.sort(employeeArray, new Comparator<Employee>() {
            @Override
            public int compare(Employee e1, Employee e2) {
                int nameDiff = e1.name.compareTo(e2.name);
                if(nameDiff != 0) { return nameDiff; }

                return e1.employeeId - e2.employeeId;
            }
        });

        for(int i = 0 ; i < employeeArray.length; i++) {
            //out.println(employeeArray[i].name);
            out.println(employeeArray[i]);
        }
    }

    static void ArrayFill() {
        int[] intArray = new int[10];

        Arrays.fill(intArray, 123);

       out.println(Arrays.toString(intArray));

        int[] ints2 = new int[10];

        Arrays.fill(ints2, 3, 5, 123) ;

        out.println(Arrays.toString(ints2));
    }

    // Searching Arrays with Arrays.binarySearch()
    static void SearchingArraysWithBinarySearch() {
        int[] ints = {0,2,4,6,8,10};

        int index = Arrays.binarySearch(ints, 6);

        out.println(index);
    }

    // Checking if Arrays are Equal with Arrays.equals()
    static void checkIfArraysAreEqual() {
        int[] ints1 = {0,2,4,6,8,10};
        int[] ints2 = {0,2,4,6,8,10};
        int[] ints3 = {10,8,6,4,2,0};

        boolean ints1EqualsInts2 = Arrays.equals(ints1, ints2);
        boolean ints1EqualsInts3 = Arrays.equals(ints1, ints3);

        out.println(ints1EqualsInts2);
        out.println(ints1EqualsInts3);
    }

    public static void main(String... args) {

        ConvertingArraysToString();

        SortingArrays();

        SortingObjects();

        ArrayFill();

        SearchingArraysWithBinarySearch();

        checkIfArraysAreEqual();

    }
}

// https://jenkov.com/tutorials/java/arrays.html
