package org.example;

import org.example.dao.ProjectDAO;
import org.example.entity.Project;
import org.example.entity.ProjectStatus;

import java.util.List;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello world!");

        ProjectDAO projectDAO = new ProjectDAO();
        Project project = new Project();
        project.setProjectName("TPO");
        project.setProjectStatus(ProjectStatus.INPROGRESS);
        projectDAO.saveProject(project);

        List<Project> projects = projectDAO.getProjects();
        projects.forEach( s -> {
            System.out.println(s.getProjectName());
            System.out.println(s.getProjectStatus());
        });
    }
}