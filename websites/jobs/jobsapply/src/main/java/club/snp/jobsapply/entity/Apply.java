package club.snp.jobsapply.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.CreationTimestamp;

import java.util.Date;

@Setter
@Getter
@Entity
@Table(name = "th_apply")
public class Apply {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    @Column(name = "title")
    private String title;
    @Column(name = "link")
    private String link;
    @Column(name = "time")
    private String time;
    @Column(name = "email")
    private String email;
    private String description;
//    @Column(name="created_date", nullable = false, updatable = false)
//    @Temporal(TemporalType.TIMESTAMP)
//    private java.util.Date dateCreated;


    @Column(name="created_date")
    @CreationTimestamp
    Date createdAt;

    @Column(name="updated_date")
    @Temporal(TemporalType.TIMESTAMP)
    private java.util.Date updatedAt;

    Apply() {}

    public Apply(String title, String link, String time) {
        this.link = link;
        this.title = title;
        this.time = time;
    }
}
