package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class HowToInvokeMethodsOfAClassUsingReflectionInJava {

    static class MyClass {
        public int myMethod(int value) {
            return value * 2;
        }
    }
    public static void main(String[] args) throws NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        // Get the Class object for the target class
        Class<?> targetClass = MyClass.class;

        // Get the Method object for the method we want to invoke
        Method method = targetClass.getMethod("myMethod", int.class);

        // Create an instance of the target class (if needed)
        Object instance = targetClass.newInstance();

        // Make the method accessible
        method.setAccessible(true);

        // Invoke the method with arguments
        int result = (int) method.invoke(instance, 42);

        // Handle the result
        System.out.println("Result: " + result);
    }
}
