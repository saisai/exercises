package java_tutorial.w3schools_com.methods;

public class MethodParam {
    public static void main(String[] args){
        checkAge(20);
    }

    static void checkAge(int age) {
        if(age < 18) {
            System.out.println("Access denied - You are not old enought");
        } else {
            System.out.println("Access granated - You are old engouth");
        }
    }
}
