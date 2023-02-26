package com.zetcode.app.json;

import org.json.JSONWriter;

public class JsonWriterEx {


    public static void main(String[] args) {

        StringBuilder user = new StringBuilder();

        JSONWriter writer = new JSONWriter(user);

        writer.object();
        writer.key("name").value("John Doe");
        writer.key("occupation").value("gardener");
        writer.key("siblings").value(2);
        writer.key("married").value(true);

        writer.key("favCols");
        writer.array();
        writer.value("red");
        writer.value("blue");
        writer.value("navy");
        writer.endArray();

        writer.endObject();

        System.out.println(user);
    }
}
