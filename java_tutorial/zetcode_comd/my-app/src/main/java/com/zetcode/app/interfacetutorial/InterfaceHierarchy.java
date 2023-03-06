package com.zetcode.app.interfacetutorial;

interface IInfo2 {
    void doInform();
}

interface IVersion2 {
    void getVersion();
}

interface ILog extends IInfo2, IVersion2 {
    void doLog();
}

class DBConnect implements ILog {

    @Override
    public void doInform(){
        System.out.println("This is DBConnect class");
    }

    @Override
    public void getVersion() {

        System.out.println("Version 1.02");
    }

    @Override
    public void doLog() {

        System.out.println("Logging");
    }

    public void connect() {

        System.out.println("Connecting to the database");
    }
}
public class InterfaceHierarchy {
    public static void main(String[] args) {

        DBConnect db = new DBConnect();
        db.doInform();
        db.getVersion();
        db.doLog();
        db.connect();
    }
}
