package java_tutorial.w3schools_com.Packages;

class OuterClassTest {

    int x = 10;

    class InnerClass {
        int y = 5;
    }
}

public class OuterClass {
    public static void main(String[] args){
        OuterClassTest myOuter = new OuterClassTest();
        OuterClassTest.InnerClass myInner = myOuter.new InnerClass();
        System.out.println(myInner.y + myOuter.x);
    }    
}
