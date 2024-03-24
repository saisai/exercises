package org.example.dao;

import org.example.entity.Project;
import org.example.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

import java.util.List;

public class ProjectDAO {
    public void saveProject(Project project) {
        try(Session session = HibernateUtil.getSessionFactory().openSession()) {
            // start a transaction
            Transaction transaction = session.beginTransaction();

            // save the proejct object
            session.persist(project);
            // commit transaction
            transaction.commit();
        }
    }

    public List<Project> getProjects() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.createQuery("from Project", Project.class).list();
        }
    }
}
