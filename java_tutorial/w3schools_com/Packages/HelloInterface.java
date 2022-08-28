package java_tutorial.w3schools_com.Packages;

interface Animal {

    public void animalSound();
    public void sleeper();

}

class Pig implements Animal {
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }

    public void sleeper() {
        System.out.println("Zzz");
    }
}

class HelloInterface {
    public static void main(String[] args){
        Pig myPig = new Pig();
        myPig.animalSound();
        myPig.sleeper();
    }
}
