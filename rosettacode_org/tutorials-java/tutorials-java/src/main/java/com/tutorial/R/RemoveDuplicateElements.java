package com.tutorial.R;

import java.util.*;

public class RemoveDuplicateElements {
    public static void main(String... args) {
        List<Integer> l1 = new ArrayList<Integer>(){{ add(1); add(2);}};
        List<Integer> l2 = new ArrayList<Integer>(){{ add(1); add(2);}};
        List<Integer> l3 = new ArrayList<Integer>(){{ add(1); add(2); add(3);}};

        Set<Integer> s1 = new HashSet<Integer>(){{ add(1); add(1);}};
        Set<Integer> s2 = new HashSet<Integer>(){{ add(1); add(1);}};
        Set<Integer> s3 = new HashSet<Integer>(){{ add(1); add(1); add(2);}};

        Map<String, String> m1 = new HashMap<String, String>(){{ put("a", "a"); put("b", "b");}};
        Map<String, String> m2 = new HashMap<String, String>(){{ put("a", "a"); put("b", "b");}};
        Map<String, String> m3 = new HashMap<String, String>(){{ put("a", "a"); put("b", "b"); put("c", "c");}};

        Object[] data = {1, 1, 2, 2, 3, 3, 3, "a", "a", "b", "b", "c", "d", 1.1, 1.1, "hello", "hello",
                        true, true, new Integer(10), new Integer(10),
                        l1, l2, l3,
                        s1, s2, s3,
                        m1, m2, m3
                    };
        Set<Object> uniqueSet = new HashSet<Object>(Arrays.asList(data));
        for(Object o : uniqueSet) {
            System.out.printf("%s ", o);
        }

        System.out.println();
        Arrays.stream(data).distinct().forEach((o) -> System.out.printf("%s ", o));
    }
}
