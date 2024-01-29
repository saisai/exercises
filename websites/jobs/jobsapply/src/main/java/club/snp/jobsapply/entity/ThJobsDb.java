package club.snp.jobsapply.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "th_jobsdb")
public class ThJobsDb {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    private String title;
    private String link;
    private String time;
    @Column(name="created_date")
    @Temporal(TemporalType.TIMESTAMP)
    private java.util.Date dateCreated;


}
