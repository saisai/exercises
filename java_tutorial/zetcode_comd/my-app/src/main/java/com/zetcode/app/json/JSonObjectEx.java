package com.zetcode.app.json;

import org.json.JSONObject;

public class JSonObjectEx {

    public static void main(String[] args) {

        JSONObject user = new JSONObject();

        user.put("name", "John Doe");
        user.put("occupation", "gardener");
        user.put("siblings", Integer.valueOf(2));
        user.put("height", Double.valueOf(172.35));
        user.put("married", Boolean.TRUE);

        String userJson = user.toString();

        System.out.println(userJson);
    }
}
