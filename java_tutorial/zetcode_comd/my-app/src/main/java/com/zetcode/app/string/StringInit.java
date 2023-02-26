package com.zetcode.app.string;

public class StringInit {

    public static void main(String[] args) {
        char[] cdb = {'M', 'y', 'S', 'Q', 'L'};

        String lang = "Java";
        String ide = new String("NetBeans");
        String db = new String(cdb);

        System.out.println(lang);
        System.out.println(ide);
        System.out.println(db);

        StringBuilder sb1 = new StringBuilder(lang);
        StringBuilder sb2 = new StringBuilder();
        sb2.append("Fields");
        sb2.append(" of ");
        sb2.append("glory");

        System.out.println(sb1);
        System.out.println(sb2);

    }
}
