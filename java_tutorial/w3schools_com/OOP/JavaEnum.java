package java_tutorial.w3schools_com.OOP;

enum Level {
    LOW,
    MEDIUM,
    HIGH
  }

public class JavaEnum {
    public static void main(String[] args) {
        Level myVar = Level.MEDIUM;
    
        switch(myVar) {
          case LOW:
            System.out.println("Low level");
            break;
          case MEDIUM:
             System.out.println("Medium level");
            break;
          case HIGH:
            System.out.println("High level");
            break;
        }
      }
}
