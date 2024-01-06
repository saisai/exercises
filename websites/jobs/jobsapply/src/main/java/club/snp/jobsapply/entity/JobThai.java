package club.snp.jobsapply.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
@Table(name = "th_jobthai")
public class JobThai {
    @Id
    private Integer id;
    private String title;
    private String link;
    private String time;
    @Column(name="created_date")
    @Temporal(TemporalType.TIMESTAMP)
    private java.util.Date dateCreated;
}
