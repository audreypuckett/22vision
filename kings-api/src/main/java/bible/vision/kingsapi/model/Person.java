package bible.vision.kingsapi.model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Entity
public class Person {
    @Id
    @GeneratedValue
    private int id;
    private String name;
    private String role;
    @ElementCollection
    private List<String> alternativeNames;
    @OneToMany
    private List<Highlight> highlights;
}
