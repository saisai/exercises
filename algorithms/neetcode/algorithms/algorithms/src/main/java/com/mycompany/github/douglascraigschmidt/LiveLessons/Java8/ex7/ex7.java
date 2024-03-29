package com.mycompany.github.douglascraigschmidt.LiveLessons.Java8.ex7;

import java.util.function.Supplier;

public class ex7 {

    public static void main(String[] args) {

        // Demonstrate how a Supplier can be used as a factory for
        // a zero-parameter constructor reference.
        zeroParamConstructorRef();

        // Demonstrate how Supplier objects can be used as factories
        // for multiple zero-parameter constructor references.
        zeroParamConstructorRefEx();

        // Demonstrate how a custom functional interface (i.e.,
        // TriFactory, which is defined below) can be used as a
        // factory for a three-parameter constructor reference.
        threeParamConstructorRef();

    }

    private static void zeroParamConstructorRef() {
        System.out.println("zeroParamConstructorRef()");

        // Assign a constructor reference to a supplier that acts as a
        // factory for a zero-param object of CrDemo.
        Supplier<CrDemo> factory = CrDemo::new;

        // Use the factory to create a new instance of CrDemo and
        // then call its run() method.
        CrDemo crDemo = factory.get();
        crDemo.run();
    }

    private static void zeroParamConstructorRefEx() {
        System.out.println("zeroParamConstructorRefEx()");

        // Assign a constructor reference to a supplier that acts as a
        // factory for a zero-param object of CrDemo.
        Supplier<CrDemo> crDemoFactory = CrDemo::new;

        // Assign a constructor reference to a supplier that acts as a
        // factory for a zero-param object of CrDemoEx.
        Supplier<CrDemoEx> crDemoExFactory = CrDemoEx::new;

        // This helper method invokes the given supplier to create a
        // new object and call its run() method.
        runDemo(crDemoFactory);
        runDemo(crDemoExFactory);
    }

    private static <T extends Runnable> void runDemo(Supplier<T> factory) {
        factory.get().run();
    }

    public static void threeParamConstructorRef() {
        System.out.println("threeParamConstructorRef()");

        // Assign a constructor reference to a customized functional
        // interface that acts as a factory to create a
        // three-parameter constructor for CrDemo.
        TriFactory<String, Integer, Long, CrDemo> factory =
                CrDemo::new;

        // Use the factory to create a new instance of CrDemo and call
        // its run() method.
        factory.of("The answer is ", 4, 2L).run();
    }

    @FunctionalInterface
    interface TriFactory<P1, P2, P3, R> {
        /**
         * Create an object of type {@code R} using the three
         * generic parameters and return the object.
         */
        R of(P1 p1, P2 p2, P3 p3);
    }
}
