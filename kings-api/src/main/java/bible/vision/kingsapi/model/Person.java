package bible.vision.kingsapi.model;

import jakarta.persistence.*;

import java.util.List;

@Entity
@Inheritance(strategy = InheritanceType.JOINED)
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

    public Person(){}

    public Person(String role){
        this.role = role;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getRole() {
        return role;
    }

    public List<String> getAlternativeNames() {
        return alternativeNames;
    }

    public List<Highlight> getHighlights() {
        return highlights;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public void setAlternativeNames(List<String> alternativeNames) {
        this.alternativeNames = alternativeNames;
    }

    public void setHighlights(List<Highlight> highlights) {
        this.highlights = highlights;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", role='" + role + '\'' +
                ", also known as =" + alternativeNames;
    }
}
