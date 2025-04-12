package bible.vision.kingsapi.data;

import bible.vision.kingsapi.model.BookEnum;
import bible.vision.kingsapi.model.Highlight;
import bible.vision.kingsapi.model.King;
import bible.vision.kingsapi.model.Person;

import java.util.ArrayList;
import java.util.List;

public class Solomon implements IMakeKing{

    private King solomon = new King();

    private void setInformation(){
        solomon.setAgeKinged(20);
        solomon.setRiegnStart("1010 BCE");
        solomon.setRiegnEnd("970 BCE");
        solomon.setYearsReigned(40);
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
        solomon.setHighlights(highlights);
    }

    @Override
    public King getKing() {
        return solomon;
    }

    @Override
    public King makeKing() {
        setInformation();
        setHighlights();
        Person mother = new Person();
        mother.setName("Unnamed Biblically");
        mother.setRole("servant of the Lord");
        solomon.setMother(mother);
        return solomon;
    }
}
