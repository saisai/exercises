package dto;

public class Address {

    private int number;
    private String road;

    public Address(int number, String road) {
        this.number = number;
        this.road = road;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getRoad() {
        return road;
    }

    public void setRoad(String road) {
        this.road = road;
    }
}
