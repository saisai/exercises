package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Method;

public class ReflectionExample {
    public static void main(String[] args) {
        String text = "Hello, Reflextion";
        // Get the class of the object
        Class<?> cls = text.getClass();

        // Get the methods of the class
        Method[] methods = cls.getMethods();
        for(Method method : methods) {
            System.out.println("Method Name: " + method.getName());
        }
    }
}
