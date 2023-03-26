package langs.systems;

import java.util.Iterator;
import java.util.Map;

public class System001 {

    private static void showEnv() {
        Map<String, String> envs = System.getenv();

        for(Map.Entry<String, String> entry : envs.entrySet()) {
            System.out.println("Key = " + entry.getKey() + ", Value =" + entry.getValue());
        }
    }

    private static void showEnv2() {
        Map<String, String> envs = System.getenv();

        // using keySet() for iteration over keys
        for (String name : envs.keySet())
            System.out.println("key: " + name);

        // using values() for iteration over values
        for (String url : envs.values())
            System.out.println("value: " + url);
    }

    private static void showEnv3() {
        Map<String, String> envs = System.getenv();

        // using iterators
        Iterator<Map.Entry<String, String>> itr = envs.entrySet().iterator();

        while(itr.hasNext())
        {
            Map.Entry<String, String> entry = itr.next();
            System.out.println("Key = " + entry.getKey() +
                    ", Value = " + entry.getValue());
        }
    }

    private static void showEnv4() {
        Map<String, String> envs = System.getenv();

        // forEach(action) method to iterate map
        envs.forEach((k, v) -> System.out.println("Key = " + k + ", Value =" + v));
    }

    // Iterating over keys and searching for values (inefficient)
    private static void showEnv5() {
        Map<String, String> envs = System.getenv();

        // looping over keys
        for (String name : envs.keySet())
        {
            // search  for value
            String url = envs.get(name);
            System.out.println("Key = " + name + ", Value = " + url);
        }
    }

    public static void main(String... args) {
//        System001.showEnv();
//        System.out.println();
//        showEnv2();
//        System.out.println();
//        showEnv3();
//        System.out.println();
//        showEnv4();
//        System.out.println();
//        showEnv5();

        System.out.println("nanoTime " + System.nanoTime());
    }



}
