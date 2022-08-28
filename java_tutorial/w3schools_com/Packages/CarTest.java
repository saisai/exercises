package java_tutorial.w3schools_com.Packages;

class Vehicle {
    protected String brand = "Ford";
    public void honk() {
        System.out.println("Tuut, tutt");
    }
}

public class CarTest extends Vehicle {

    private String modelName = "Mustang";
    public static void main(String[] args){
        CarTest myFastCar = new CarTest();
        myFastCar.honk();
        System.out.println(myFastCar.brand + " " + myFastCar.modelName);
    }
    
}
