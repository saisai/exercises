package java_tutorial.w3schools_com.OOP;

import java.util.ArrayList;

public class JavaArrayList {

    public static void main(String[] args){
        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);
        for( int i = 0; i < cars.size(); i++){
            System.out.println(cars.get(i));
        }

        for(String i: cars) {
            System.out.println(i);
        }
    }
    
}
