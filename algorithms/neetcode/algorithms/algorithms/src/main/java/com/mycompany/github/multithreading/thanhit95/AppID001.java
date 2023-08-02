package com.mycompany.github.multithreading.thanhit95;

public class AppID001 {
    public static void main(String[] args) {
        Runnable doTask = () -> {
            long id = Thread.currentThread().getId();
            System.out.println(id);
        };



        int i = 0;
        for(;;) {
            if(i > 3)
                break;
            i++;
            System.out.println("i => " + i);
            Thread thFoo = new Thread(doTask);
            Thread thBar = new Thread(doTask);

            System.out.println("foo's id: " + thFoo.getId());
            System.out.println("bar's id: " + thBar.getId());
            thFoo.start();
            thBar.start();
        }

        Thread thFoo = new Thread(doTask);
        Thread thBar = new Thread(doTask);

        System.out.println("foo's id: " + thFoo.getId());
        System.out.println("bar's id: " + thBar.getId());
        thFoo.start();
        thBar.start();

    }
}
