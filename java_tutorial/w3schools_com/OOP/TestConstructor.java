package java_tutorial.w3schools_com.OOP;

public class TestConstructor {
    int x;

    // create a class constructor for the Main class
    public TestConstructor() {
        x = 5;
    }

    public static void  main(String[] args){
        TestConstructor myObj = new TestConstructor();
        System.out.println(myObj.x);
    }
}
