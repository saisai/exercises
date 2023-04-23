package com.tutorial.F;

import java.util.LinkedList;
import java.util.List;

public class FlattenUtil15 {
    public static void flatten(List<?> fromTreeList, List<Object> toFlatList) {
        for(Object item : fromTreeList) {
            if(item instanceof List<?>) {
                flatten((List<?>) item, toFlatList);
            } else {
                toFlatList.add(item);
            }
        }
    }

    public static List<Object> flatten(List<?> list) {
        List<Object> retVal = new LinkedList<Object>();
        flatten(list, retVal);
        return retVal;
    }
}
