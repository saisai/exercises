package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Modifier;
import java.util.Arrays;

public class ConstructorReflectionExample {

    class MyClass {
        public MyClass() {
        }

        public MyClass(int value) {
        }

        private MyClass(String name) {
        }
    }
    public static void main(String[] args) {
        Class<?> targetClass = MyClass.class;

        Constructor<?>[] constructors = targetClass.getDeclaredConstructors();

        for (Constructor<?> constructor : constructors) {
            String constructorName = constructor.getName();
            Class<?>[] parameterTypes = constructor.getParameterTypes();
            int modifiers = constructor.getModifiers();

            System.out.println("Constructor Name: " + constructorName);
            System.out.println("Parameter Types: " + Arrays.toString(parameterTypes));
            System.out.println("Modifiers: " + Modifier.toString(modifiers));
            System.out.println();
        }
    }
}
