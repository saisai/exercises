package club.snp.jobsapply.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity
@Table(name="tb_position")
public class Position {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    @Column(name = "title")
    private String title;

    private String description;

    Position() {}

    public Position(String title, String description) {
        this.title = title;
        this.description = description;
    }
}
