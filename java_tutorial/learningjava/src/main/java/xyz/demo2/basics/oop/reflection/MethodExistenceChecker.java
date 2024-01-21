package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Method;

public class MethodExistenceChecker {
    static class MyClass {
        public void myMethod() {
            // Method implementation
        }
    }
    public static boolean doesMethodExist(Class<?> clazz, String methodName) {
        Method[] methods = clazz.getDeclaredMethods();
        for (Method method : methods) {
            if (method.getName().equals(methodName)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Class<?> myClass = MyClass.class;
        String methodName = "myMethod";

        boolean methodExists = doesMethodExist(myClass, methodName);
        System.out.println("Method exists: " + methodExists);
    }
}
