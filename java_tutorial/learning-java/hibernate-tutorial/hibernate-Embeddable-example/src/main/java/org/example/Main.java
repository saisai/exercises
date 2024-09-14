package org.example;

import org.example.entity.Address;
import org.example.entity.Name;
import org.example.entity.User;
import org.example.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");

        Name name = new Name("Ramesh", "M", "Fadatare");
        Address address = new Address("111", "Puadroad", "Pune", "Maharastra", "India", "411038");
        User user = new User(name, "ramesh@gmail.com", address);

        Transaction transaction = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            // start a transaction
            transaction = session.beginTransaction();
            // save the student object
            session.persist(user);
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