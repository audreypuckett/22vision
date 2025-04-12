package bible.vision.kingsapi.data;

import bible.vision.kingsapi.model.*;

import java.util.ArrayList;
import java.util.List;

public class David implements IMakeKing{

    private King david = new King();

    private void setInformation(){
        david.setStatus(StatusEnum.DID_RIGHT);
        david.setKingdom(KingsEnum.UNITED);
        david.setAgeKinged(30);
        david.setRiegnStart("1010 BCE");
        david.setRiegnEnd("970 BCE");
        david.setYearsReigned(40);
    }

    private void setHighlights(){
        List<Highlight> highlights = new ArrayList<>();
        Highlight highlight = new Highlight(
                BookEnum.SECOND_SAMUEL,
                11,
                "2-5",
                "Slept with Bethsheda, a married woman who was in process of purification after monthly uncleanlinesss. " +
                        "They conceived a child"
        );
        Highlight highlight2 = new Highlight(
                BookEnum.SECOND_SAMUEL,
                11,
                "6-27",
                "Tried to get Bethsheda's husband to go home so the true father would be concealed." +
                        "When he was unsuccessful, he placed Uriah at the front lines to die." +
                        "He died." +
                        "'27 - the thing David had done displeased the LORD'"
        );
        Highlight highlight3 = new Highlight(
                BookEnum.SECOND_SAMUEL,
                12,
                "13-14",
                "Sinned acknowledged, taken away, and punishment decreed." +
                        "20 - After everything worshipped the LORD"
        );
        highlights.add(highlight);
        highlights.add(highlight2);
        highlights.add(highlight3);
        david.setHighlights(highlights);
    }

    @Override
    public King getKing() {
        return david;
    }

    @Override
    public King makeKing() {
        setInformation();
        setHighlights();
        setFather();
        Person mother = new Person();
        mother.setName("Unnamed Biblically");
        mother.setRole("servant of the Lord");
        david.setMother(mother);
        return david;
    }

    public void setFather() {
        Person jesse = new Person();
        jesse.setName("Jesse");
        jesse.setRole("Servant of the Lord");
        david.setFather(jesse);
    }
}
