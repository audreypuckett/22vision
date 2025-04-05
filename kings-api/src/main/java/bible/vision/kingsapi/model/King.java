package bible.vision.kingsapi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class King extends Person{

    private String riegnStart;
    private String riegnEnd;
    private int ageKinged;
    private int yearsReigned;
    private int monthsReigned;
    @ManyToOne
    @JoinColumn(name = "father_id")
    private Person father;
    @ManyToOne
    @JoinColumn(name = "mother_id")
    private Person mother;
    @ManyToOne
    @JoinColumn(name = "predecessor_id")
    private King predecessor;

    public King(){
        super("King");
    }
}
