package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Method;
import java.lang.reflect.Parameter;

public class ReflectionParameterExample {

    static class MyClass {
        public void myMethod(int param1, String param2) {
            // Method implementation
        }
    }
    public static void main(String[] args) throws NoSuchMethodException {
        Class<?> myClass = MyClass.class;
        Method myMethod = myClass.getDeclaredMethod("myMethod", int.class, String.class);

        Parameter[] parameters = myMethod.getParameters();

        for (Parameter parameter : parameters) {
            String paramName = parameter.getName();
            Class<?> paramType = parameter.getType();
            int modifiers = parameter.getModifiers();

            System.out.println("Parameter Name: " + paramName);
            System.out.println("Parameter Type: " + paramType.getName());
            System.out.println("Modifiers: " + modifiers);
        }
    }
}
