package com.zetcode.app.interfacetutorial;

interface Device {
    void switchOn();
    void switchOff();
}
interface Volume {
    void volumeUp();
    void volumeDown();
}

interface Pluggable {
    void plugIn();
    void plugOff();
}

class CellPhone implements Device, Volume, Pluggable {
    @Override
    public void switchOn() {
        System.out.println("Switching on");
    }

    @Override
    public void switchOff() {
        System.out.println("Switching off");
    }

    @Override
    public void volumeUp() {
        System.out.println("Volume up");
    }

    @Override
    public void volumeDown() {
        System.out.println("Volume Down");
    }

    @Override
    public void plugIn() {

        System.out.println("Plugging in");
    }

    @Override
    public void plugOff() {

        System.out.println("Plugging off");
    }
}

public class MultipleInterfaces {

    public static void main(String[] args) {
        CellPhone cp = new CellPhone();
        cp.switchOn();
        cp.volumeUp();
        cp.plugIn();
    }
}
