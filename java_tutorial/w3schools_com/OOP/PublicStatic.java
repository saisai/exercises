package java_tutorial.w3schools_com.OOP;

public class PublicStatic {
    public static void main(String[] args){

        myStaticMethod(); // Call the static method

        PublicStatic myObj = new PublicStatic(); // Create an object of MyClass
        myObj.myPublicMethod(); // Call the public method

    }

    // static method
    static void myStaticMethod(){
        System.out.println("Static methods can be called without creating objects");
    }

    // Public method
  public void myPublicMethod() {
    System.out.println("Public methods must be called by creating objects");
  }
}
