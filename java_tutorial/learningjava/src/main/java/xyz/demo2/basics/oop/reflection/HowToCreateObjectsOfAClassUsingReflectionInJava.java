package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class HowToCreateObjectsOfAClassUsingReflectionInJava {

    static class YourClass {
        private String name;

        public YourClass() {
            this.name = "Default Name";
        }

        public YourClass(String name) {
            this.name = name;
        }
    }
    public static void main(String[] args) {
        try {
            Class<?> clazz = YourClass.class;
            Constructor<?> constructor = clazz.getDeclaredConstructor(String.class);
            constructor.setAccessible(true);
            YourClass instance = (YourClass) constructor.newInstance("John");

            System.out.println("Created object with name: " + instance.name);
        } catch (InstantiationException | IllegalAccessException | IllegalArgumentException |
                 InvocationTargetException | NoSuchMethodException e) {
            e.printStackTrace();
        }
    }
}
