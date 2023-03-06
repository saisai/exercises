package com.springtutorials.tutorials.onetomany.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import javax.persistence.*;

@Entity
@Table(name="comments")
public class Comment {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "comment_generator")
    private long id;

    @Lob
    private String content;

    @ManyToOne(fetch=FetchType.LAZY, optional=false)
    @JoinColumn(name="tutorials2_id", nullable = false)
    @OnDelete(action= OnDeleteAction.CASCADE)
    @JsonIgnore
    private Tutorial2 tutorials2;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public Tutorial2 getTutorial() {
        return tutorials2;
    }

    public void setTutorial(Tutorial2 tutorials2) {
        this.tutorials2 = tutorials2;
    }
}
