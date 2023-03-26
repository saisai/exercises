package com.tutorial.R;

import java.security.SecureRandom;

public class RandomNumberGeneratorDevice {
    public static void main(String... args) {
        SecureRandom rng = new SecureRandom();

        // Prints a random signed 32-big integer.
        System.out.println(rng.nextInt());
    }
}
