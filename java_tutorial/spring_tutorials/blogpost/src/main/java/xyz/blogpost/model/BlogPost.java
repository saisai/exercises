package xyz.blogpost.model;

import org.hibernate.annotations.CreationTimestamp;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import java.util.Date;
import java.util.Objects;

@Entity
@Table(name="blogposts")
public class BlogPost {
    @Id
    //@GeneratedValue(strategy = GenerationType.AUTO)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;


    @NotEmpty(message ="Title is mandatory")
    String title;
    @NotEmpty(message ="Link is mandatory")
    String link;

    String description;

//    @Column(
//            name = "CREATED_AT",
//            updatable = false
//    )
//    @Temporal(TemporalType.TIMESTAMP)
    @CreationTimestamp
    Date createdAt;

    @Column(
            name = "UPDATED_AT"
    )
    @Temporal(TemporalType.TIMESTAMP)
    Date updatedAt;

    @Column(name = "delete")
    private Integer delete = 0;


    public BlogPost() {

    }

    public BlogPost(String title, String link, String description,  Date updated_at) {
        this.title = title;
        this.link = link;
        this.description = description;
        //this.createdAt = created_at;
        this.updatedAt = updated_at;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date created_at) {
        this.createdAt = created_at;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }


    public void setDelete(Integer delete) {
        this.delete = delete;
    }

    public Integer getDelete() {
        return delete;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        BlogPost blogPost = (BlogPost) o;
        return Objects.equals(id, blogPost.id) && Objects.equals(title, blogPost.title) && Objects.equals(link, blogPost.link) && Objects.equals(description, blogPost.description) && Objects.equals(createdAt, blogPost.createdAt) && Objects.equals(updatedAt, blogPost.updatedAt);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, title, link, description, createdAt, updatedAt);
    }

    @Override
    public String toString() {
        return "BlogPost{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", link='" + link + '\'' +
                ", description='" + description + '\'' +
                ", created_at=" + createdAt +
                ", updated_at=" + updatedAt +
                '}';
    }
}
