package club.snp.jobsapply.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;


@Setter
@Getter
@Entity
@Table(name="tb_file")
public class File {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    Integer id;
    @Column(name = "title")
    String title;

//    @ManyToOne(cascade = CascadeType.ALL)
//    @JoinColumn(name="position_id")
//    Position position;


    @JsonProperty
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "position_id", nullable = false)
    @OnDelete(action = OnDeleteAction.CASCADE)
    Position position;

    public File() {}

    public File(String title) {
        this.title = title;
    }

    public Position getPosition() { return position; }
    public void setPosition(Position position) { this.position = position; }
}
