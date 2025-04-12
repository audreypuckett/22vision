package bible.vision.kingsapi.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Highlight {
    @Id
    @GeneratedValue
    private String id;
    private BookEnum book;
    private String note;
    private int chapter;
    private String verse;

    public Highlight() {}
    public Highlight(BookEnum book, int chapter, String verse, String note) {
        this.book = book;
        this.chapter = chapter;
        this.verse = verse;
        this.note = note;
    }

    public String getId() {
        return id;
    }

    public BookEnum getBook() {
        return book;
    }

    public String getNote() {
        return note;
    }

    public int getChapter() {
        return chapter;
    }

    public String getVerse() {
        return verse;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setBook(BookEnum book) {
        this.book = book;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public void setChapter(int chapter) {
        this.chapter = chapter;
    }

    public void setVerse(String verse) {
        this.verse = verse;
    }

    @Override
    public String toString() {
        return "Highlight{" +
                note +
                '\'' + book + " " + chapter + ":" + verse +
                '}';
    }
}
