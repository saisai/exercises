package com.springtutorials.tutorials.onetomany.model;

import javax.persistence.*;

@Entity
@Table(name="tutorials2")
public class Tutorial2 {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "tutorials2_generator")
    private long id;

    @Column(name="title")
    private String title;

    @Column(name="description")
    private String description;

    @Column(name="published")
    private boolean published;

    public Tutorial2() {

    }

    public Tutorial2(String title, String description, boolean published) {
        this.title = title;
        this.description = description;
        this.published = published;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public boolean isPublished() {
        return published;
    }

    public void setPublished(boolean published) {
        this.published = published;
    }
}

