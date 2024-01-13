package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Method;

public class MethodReflectionExample {

    class MyClass {
        public void method1(int x, String y) {
            // Implementation
        }

        private double method2() {
            // Implementation
            return 0.0;
        }

        protected void method3() {
            // Implementation
        }
    }
    public static void main(String[] args) {
        Class<?> targetClass = MyClass.class;

        Method[] methods = targetClass.getDeclaredMethods();

        for (Method method : methods) {
            String methodName = method.getName();
            Class<?> returnType = method.getReturnType();
            Class<?>[] parameterTypes = method.getParameterTypes();

            System.out.println("Method Name: " + methodName);
            System.out.println("Return Type: " + returnType.getName());

            System.out.print("Parameter Types: ");
            for (Class<?> paramType : parameterTypes) {
                System.out.print(paramType.getName() + " ");
            }
            System.out.println();
        }
    }
}
