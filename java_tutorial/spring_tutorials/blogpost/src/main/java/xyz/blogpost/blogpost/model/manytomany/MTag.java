package xyz.blogpost.blogpost.model.manytomany;


import org.hibernate.annotations.NaturalId;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "mtags")
public class MTag {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull
    @Size(max = 100)
    @NaturalId
    private String name;

    @ManyToMany(fetch = FetchType.LAZY,
            cascade = {
                    CascadeType.PERSIST,
                    CascadeType.MERGE
            },
            mappedBy = "mtags")
    private Set<MPost> posts = new HashSet<>();

    public MTag() {

    }

    public MTag(String name) {
        this.name = name;
    }

    // Getters and Setters (Omitted for brevity)

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Set<MPost> getMPosts() {
        return posts;
    }

    public void setMPosts(Set<MPost> posts) {
        this.posts = posts;
    }
}