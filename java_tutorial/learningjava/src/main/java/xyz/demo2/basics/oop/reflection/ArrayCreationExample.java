package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Array;

public class ArrayCreationExample {

    static class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    '}';
        }
    }
    public static void main(String[] args) {
        // Creating an int array of size 5
        int[] intArray = (int[]) Array.newInstance(int.class, 5);
        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = i * 2;
        }
        // Creating a String array of size 3
        String[] stringArray = (String[]) Array.newInstance(String.class, 3);
        stringArray[0] = "Hello";
        stringArray[1] = "World";
        stringArray[2] = "!";

        // Creating an array of custom objects
        Person[] personArray = (Person[]) Array.newInstance(Person.class, 2);
        personArray[0] = new Person("John", 30);
        personArray[1] = new Person("Alice", 25);

//         Printing the arrays
        printArrayTest(intArray);
        printArrayTest(stringArray);
        printArrayTest(personArray);
    }
//     Helper method to print an array
    public static void printArrayTest(Object array) {
        int length = Array.getLength(array);
        for (int i = 0; i < length; i++) {
            System.out.println(Array.get(array, i));
        }
    }
}
