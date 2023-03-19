package dto;

import dto.Address;

import java.util.List;

public class Student {

    private int age;
    private String name;

    private List<Address> addresses;

    public Student(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public Student(int age, String name, List<Address> addresses) {
        this.age = age;
        this.name = name;
        this.addresses = addresses;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Address> getAddresses() {
        return addresses;
    }

    public void setAddresses(List<Address> addresses) {
        this.addresses = addresses;
    }

    @Override
    public String toString() {
        return String.format("Student %d \t %s", age, name);
    }
}
