package org.example;

import org.example.entity.Student;
import org.example.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

import java.util.List;

public class Main {
    public static void main(String[] args) {

        saveStudent();

        Transaction transaction = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            transaction = session.beginTransaction();
            // Executing named queries

            List<Object> totalStudents = session.createNamedQuery("GET_STUDENTS_COUNT").getResultList();
            System.out.println("Total Students: " + totalStudents.get(0));

            List < Object > student = session.createNamedQuery("GET_STUDENT_BY_ID").setParameter("id", 1).getResultList();

            System.out.println(student.get(0));

            List <Student> students = session.createNamedQuery("GET_ALL_STUDENTS", Student.class).getResultList();
            for (Student student1: students) {
                System.out.println("ID : " + student1.getId() + " \tNAME : " + student1.getFirstName());
            }

            transaction.commit();

        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            e.printStackTrace();
        }

    }

    private static void saveStudent() {
        Transaction transaction = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {

            // start a transaction
            transaction = session.beginTransaction();
            // create new student
            Student student = new Student("Ramesh", "Fadatare", "rameshfadatare@javaguides.com");
            // save the student object
            session.persist(student);
            // commit transaction
            transaction.commit();
        } catch (Exception e) {
            if (transaction != null) {
                transaction.rollback();
            }
            e.printStackTrace();
        }
    }
}