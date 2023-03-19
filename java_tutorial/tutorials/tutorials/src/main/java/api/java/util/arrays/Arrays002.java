package api.java.util.arrays;

import dto.Address;
import dto.Student;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Arrays002 {

    public static void main(String... args) {

        List<Address> address = new ArrayList<Address>();
        address.add(new Address(10, "Road 1"));
        address.add(new Address(11, "Road 2"));

        List<Address> address2 = new ArrayList<Address>(
                Arrays.asList(
                        new Address(12, "Road 3"),
                        new Address(13, "Road 4")
                )
        );



        List<Student> student = new ArrayList<Student>();
        student.add(new Student(20, "Name 001", address));
        student.add(new Student(30, "Name 002", address2));

        System.out.println("Size " + student.size());


        for(Student stu : student) {
            System.out.println(stu.getName());
            Arrays.stream(stu.getAddresses().toArray(new Address[0]))
                    .forEach(e -> System.out.format("%d %s \n",e.getNumber(), e.getRoad()));
                    //.forEach(e -> System.out.print(e.getNumber() + " " + e.getRoad()));
            System.out.println();
//            System.out.format("Student name is %s and address is %d, %s", stu.getName(), stu.getAddresses().get(idx).getNumber(),
//                    stu.getAddresses().get(idx).getRoad());

        }

        // convert List objects to Arrays
//        Student[] stArray = student.toArray(new Student[0]);
//
//        System.out.println("Size :  " + stArray.length);
//
//        Arrays.stream(stArray)
//                .forEach(e -> System.out.println(e.getName()));
//
//        System.out.println("tesing ");
//
//
//        List<Student> stNames = Arrays.stream(stArray)
//                .filter(e -> e.getName().equals("Name 001"))
//                .peek( e -> System.out.println("Filter value " + e.getName()))
//                .collect(Collectors.toList());
//
//        System.out.println("testing 2");
//
//        for(Student st : stNames) {
//            System.out.println("Hello " + st);
//        }

    }
}
