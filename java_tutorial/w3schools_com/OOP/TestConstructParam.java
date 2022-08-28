package java_tutorial.w3schools_com.OOP;

public class TestConstructParam {
    int x;

    public TestConstructParam(int y) {
        x = y;
    }

    public static void main(String[] args){
        TestConstructParam myObj = new TestConstructParam(5);
        System.out.println(myObj.x);
    }
}
