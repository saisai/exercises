package xyz.demo2.basics.oop.reflection;

public class HowToUseTypenameClassToLoadJavaClass {

    static class MyClass {
        public void sayHello() {
            System.out.println("Hello, world!");
        }
    }

    public static void main(String[] args) throws InstantiationException, IllegalAccessException {
        Class<MyClass> clazz = MyClass.class;

        // Create an instance of MyClass dynamically
        MyClass instance = clazz.newInstance();

        // Call a method on the dynamically created instance
        instance.sayHello();
    }
}
