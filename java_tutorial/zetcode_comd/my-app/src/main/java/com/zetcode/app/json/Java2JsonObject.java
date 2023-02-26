package com.zetcode.app.json;

import org.json.JSONObject;

public class Java2JsonObject {
    public static void main(String[] args) {

        User user = new User("John Doe", "gardener",
                2, 172.35, true);

        JSONObject userjo = new JSONObject(user);

        System.out.println(userjo);

        System.out.println(userjo.get("name"));
        System.out.println(userjo.get("occupation"));
        System.out.println(userjo.get("siblings"));
    }
}
