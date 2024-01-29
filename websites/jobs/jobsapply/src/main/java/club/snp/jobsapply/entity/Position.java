package club.snp.jobsapply.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

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

//    @OneToMany(fetch = FetchType.LAZY, mappedBy = "position", cascade = CascadeType.ALL)
//    private List<File> fileList;


    Position() {}

    public Position(String title, String description) {
        this.title = title;
        this.description = description;
    }

//    public List<File> getBlogList() { return fileList; }
//    public void setBlogList(List<File> blogList) { this.fileList = fileList; }

}
