package packages.lombok;

import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;

@Setter @Getter
public class User {

    private Long id;
    private String username;
    private String firstName;
    private String lastName;
    private String email;
    private LocalDate lastUpdated;
    private boolean active;
}
