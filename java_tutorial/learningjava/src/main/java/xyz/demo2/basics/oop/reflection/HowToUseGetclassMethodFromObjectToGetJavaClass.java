package xyz.demo2.basics.oop.reflection;

public class HowToUseGetclassMethodFromObjectToGetJavaClass {
    public static void main(String[] args) {
        // Create an object
        String str = "Hello, World!";

        // Use getClass() to get the class of the object
        Class<?> clazz = str.getClass();

        // Print the class name
        System.out.println("Class name: " + clazz.getName());

        // Create an object
        Object obj = "Hello, World!";

        // Check if the object is a String
        if (obj.getClass() == String.class) {
            System.out.println("It's a String!");
        } else {
            System.out.println("It's not a String!");
        }

        class Animal {}
        class Dog extends Animal {}

        // Create an object of a subclass
        Animal animal = new Dog();

        // Use getClass() to get the class of the object
        Class<?> clazzx = animal.getClass();

        // Print the class name
        System.out.println("Class name: " + clazzx.getName());
    }
}
