package com.springtutorials.tutorials.manytomany.model;

import com.fasterxml.jackson.annotation.JsonIgnore;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name="tags")
public class Tag {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name="name")
    private String name;

    @ManyToMany(fetch=FetchType.LAZY, cascade = {
            CascadeType.PERSIST,
            CascadeType.MERGE
    },
    mappedBy = "tags")
    @JsonIgnore
    private Set<Tutorial3> tutorials3 = new HashSet<>();

    public Tag() {

    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public Set<Tutorial3> getTutorials() {
        return tutorials3;
    }

    public void setTutorials3(Set<Tutorial3> tutorials) {
        this.tutorials3 = tutorials;
    }
}
