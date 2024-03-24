package org.example;

import org.example.dao.CourseDao;
import org.example.dao.InstructorDao;
import org.example.entity.Course;
import org.example.entity.Instructor;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");
        InstructorDao instructorDao = new InstructorDao();
        CourseDao courseDao = new CourseDao();

        Instructor instructor = new Instructor("Ramesh", "Fadatare", "ramesh@javaguides.com");
        instructorDao.saveInstructor(instructor);

        // create some courses
        Course tempCourse1 = new Course("Air Guitar - The Ultimate Guide");
        tempCourse1.setInstructor(instructor);
        courseDao.saveCourse(tempCourse1);

        Course tempCourse2 = new Course("The Pinball Masterclass");
        tempCourse2.setInstructor(instructor);
        courseDao.saveCourse(tempCourse2);
    }
}