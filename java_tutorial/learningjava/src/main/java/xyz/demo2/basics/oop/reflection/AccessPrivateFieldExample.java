package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Field;

public class AccessPrivateFieldExample {
    static class SomeClass {
        private String fieldName = "OriginalValue";
    }
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        SomeClass obj = new SomeClass();

        Field privateField = SomeClass.class.getDeclaredField("fieldName");
        privateField.setAccessible(true);

        // Reading the private field
        Object fieldValue = privateField.get(obj);
        System.out.println("Original Value: " + fieldValue);

        // Modifying the private field
        privateField.set(obj, "NewValue");
        fieldValue = privateField.get(obj);
        System.out.println("Modified Value: " + fieldValue);
    }

}
