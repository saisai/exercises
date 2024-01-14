package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class HowToDoDeepReflectionAcrossModulesInJava {
    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        Class<?> clazz = Class.forName("xyz.demo2.basics.oop.reflection.ConstructorReflectionExample");
        Object instance = clazz.getDeclaredConstructor().newInstance();
        Method method = clazz.getDeclaredMethod("someMethod");
        method.invoke(instance);
    }
}
