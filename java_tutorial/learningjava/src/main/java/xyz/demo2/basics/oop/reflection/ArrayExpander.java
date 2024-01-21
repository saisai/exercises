package xyz.demo2.basics.oop.reflection;

import java.lang.reflect.Array;
import java.util.Arrays;

public class ArrayExpander {
    public static Object expandArray(Object oldArray, int newSize) {
        Class<?> oldArrayType = oldArray.getClass();

        if (!oldArrayType.isArray()) {
            throw new IllegalArgumentException("Input object is not an array");
        }

        Class<?> componentType = oldArrayType.getComponentType();

        if (componentType.isPrimitive()) {
            // If it's a primitive array, you cannot directly use reflection to expand it.
            // You should consider using an Object array instead.
            throw new IllegalArgumentException("Cannot expand primitive arrays using reflection");
        }

        int oldSize = Array.getLength(oldArray);
        Object newArray = Array.newInstance(componentType, newSize);

        // Copy elements from the old array to the new array
        System.arraycopy(oldArray, 0, newArray, 0, oldSize);

        return newArray;
    }

    public static void main(String[] args) {
        // Example usage:
        String[] oldArray = new String[]{"A", "B", "C"};
        int newSize = 5;
        String[] expandedArray = (String[]) expandArray(oldArray, newSize);

        // Print the expanded array
        System.out.println(Arrays.toString(expandedArray));
    }
}
