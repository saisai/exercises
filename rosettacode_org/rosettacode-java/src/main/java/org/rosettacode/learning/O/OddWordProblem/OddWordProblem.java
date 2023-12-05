package org.rosettacode.learning.O.OddWordProblem;

public class OddWordProblem {
    interface CardHandler {
        CardHandler handle(char c) throws Exception;
    }
    final CardHandler fwd = new CardHandler() {
        @Override
        public CardHandler handle(char c){
            System.out.print(c);
            return (Character.isLetter(c) ? fwd : rev);
        }
    };

    class Reverser extends Thread implements CardHandler {
        Reverser() {
            setDaemon(true);
            start();
        }

        private Character ch; // for inter-thread comms
        private char recur() throws Exception {
            notify();
            while(ch == null) wait();
            char c = ch, ret = c;
            ch = null;
            if(Character.isLetter(c)) {
                ret = recur();
                System.out.print(c);
            }
            return ret;
        }

        public synchronized void run() {
            try {
                while(true) {
                    System.out.print(recur());
                    notify();
                }
            } catch (Exception e) {}
        }


        public synchronized CardHandler handle(char c) throws Exception {
            while(ch != null) wait();
            ch = c;
            notify();
            while(ch != null) wait();
            return (Character.isLetter(c) ? rev : fwd);
        }
    }

    final CardHandler rev = new Reverser();

    public void loop() throws  Exception {
        CardHandler handler = fwd;
        int c;
        while((c = System.in.read()) >= 0) {
            handler = handler.handle((char) c);
        }
    }

    public static void main(String[] args) throws Exception {
        new OddWordProblem().loop();
    }
}
