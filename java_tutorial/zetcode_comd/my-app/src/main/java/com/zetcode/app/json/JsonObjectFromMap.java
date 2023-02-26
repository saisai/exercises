package com.zetcode.app.json;

import netscape.javascript.JSObject;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class JsonObjectFromMap {

    public static void main(String[] args) {
        Map<String, String> data = new HashMap<String, String>();

        data.put("name", "John Doe");
        data.put("occupation", "gardener");
        data.put("siblings", "2");
        data.put("height", "172.35");
        data.put("married", "true");

        JSONObject user = new JSONObject(data) ;
        String userJson = user.toString();

        System.out.println(userJson);


    }
}
