package com.zetcode.app.json;

import org.json.JSONArray;
import org.json.JSONObject;

public class JsonArrayEx {

    public static void main(String[] args) {

        JSONObject user = new JSONObject();

        user.put("name", "John Doe");
        user.put("occupation", "gardener");
        user.put("siblings", Integer.valueOf(2));
        user.put("height", Double.valueOf(172.35));
        user.put("married", Boolean.TRUE);

        JSONArray cols = new JSONArray();
        cols.put("red");
        cols.put("blue");
        cols.put("navy");

        user.put("favCols", cols);

        String userJson = user.toString();

        System.out.println(userJson);
    }

}
