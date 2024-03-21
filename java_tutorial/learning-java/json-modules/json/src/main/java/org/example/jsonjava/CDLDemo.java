package org.example.jsonjava;

import org.json.CDL;
import org.json.JSONArray;
import org.json.JSONTokener;

public class CDLDemo {

    public static void jsonArrayFromCDT() {
        JSONArray ja = CDL.rowToJSONArray(new JSONTokener("England, USA, Canada"));
        System.out.println(ja);
    }
    public static void main(String[] args) {
        System.out.println("8.1. Producing JSONArray Directly from Comma Delimited Text: ");
        jsonArrayFromCDT();
    }
}
