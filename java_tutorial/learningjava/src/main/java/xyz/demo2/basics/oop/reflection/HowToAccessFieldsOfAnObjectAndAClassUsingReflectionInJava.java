package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Field;

public class HowToAccessFieldsOfAnObjectAndAClassUsingReflectionInJava {

    static class MyClass {
        private String fieldName = "Hello, World!";
        private static String staticFieldName = "Static Field Value";
    }
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        // Create an instance of the object
        MyClass myObject = new MyClass();

        // Get the class of the object
        Class<?> clazz = myObject.getClass();

        // Access a field by its name
        Field field = clazz.getDeclaredField("fieldName");

        // Make the field accessible (if it's not already accessible)
        field.setAccessible(true);
        // Get the value of the field from the object
        Object value = field.get(myObject);

        // Print the field value
        System.out.println(value);


        // Access a static field by its name
        Field fieldz = clazz.getDeclaredField("staticFieldName");

        // Make the field accessible (if it's not already accessible)
        fieldz.setAccessible(true);//    ww    w .   de  m   o   2 s   .c   o  m

        // Get the value of the static field from the class
        Object valuez = fieldz.get(null); // Pass null since it's a static field

        // Print the static field value
        System.out.println(valuez);
    }
}
