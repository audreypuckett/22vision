package bible.vision.kingsapi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
public class Highlight {
    @Id
    @GeneratedValue
    private String id;
    private BookEnum book;
    private String note;
    private int chapter;
    private int verse;

    @Override
    public String toString() {
        return "Highlight{" +
                note +
                '\'' + book + " " + chapter + ":" + verse +
                '}';
    }
}
