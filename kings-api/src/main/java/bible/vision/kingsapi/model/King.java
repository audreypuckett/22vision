package bible.vision.kingsapi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity
public class King extends Person{

    private KingsEnum kingdom;
    private StatusEnum status;
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

    public KingsEnum getKingdom() {
        return kingdom;
    }

    public StatusEnum getStatus() {
        return status;
    }

    public String getRiegnStart() {
        return riegnStart;
    }

    public String getRiegnEnd() {
        return riegnEnd;
    }

    public int getAgeKinged() {
        return ageKinged;
    }

    public int getYearsReigned() {
        return yearsReigned;
    }

    public int getMonthsReigned() {
        return monthsReigned;
    }

    public Person getFather() {
        return father;
    }

    public Person getMother() {
        return mother;
    }

    public King getPredecessor() {
        return predecessor;
    }

    public void setKingdom(KingsEnum kingdom) {
        this.kingdom = kingdom;
    }

    public void setStatus(StatusEnum status) {
        this.status = status;
    }

    public void setRiegnStart(String riegnStart) {
        this.riegnStart = riegnStart;
    }

    public void setRiegnEnd(String riegnEnd) {
        this.riegnEnd = riegnEnd;
    }

    public void setAgeKinged(int ageKinged) {
        this.ageKinged = ageKinged;
    }

    public void setYearsReigned(int yearsReigned) {
        this.yearsReigned = yearsReigned;
    }

    public void setMonthsReigned(int monthsReigned) {
        this.monthsReigned = monthsReigned;
    }

    public void setFather(Person father) {
        this.father = father;
    }

    public void setMother(Person mother) {
        this.mother = mother;
    }

    public void setPredecessor(King predecessor) {
        this.predecessor = predecessor;
    }

    @Override
    public String toString() {
        return "King{" +
                "kingdom=" + kingdom +
                ", status=" + status +
                ", riegnStart='" + riegnStart + '\'' +
                ", riegnEnd='" + riegnEnd + '\'' +
                ", ageKinged=" + ageKinged +
                ", yearsReigned=" + yearsReigned +
                ", monthsReigned=" + monthsReigned +
                ", father=" + father +
                ", mother=" + mother +
                ", predecessor=" + predecessor +
                '}';
    }
}
